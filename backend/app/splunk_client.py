import os
import time
from pathlib import Path

from dotenv import load_dotenv
import httpx

# Load environment from .env if present
load_dotenv()

SPLUNK_BASE_URL = os.environ.get("SPLUNK_BASE_URL", "")
SPLUNK_TOKEN = os.environ.get("SPLUNK_TOKEN", "")
SPLUNK_VERIFY_SSL = os.environ.get("SPLUNK_VERIFY_SSL", "true").lower() in ("1", "true", "yes")


def _headers() -> dict[str, str]:
    headers = {"Accept": "application/json"}
    if SPLUNK_TOKEN:
        headers["Authorization"] = f"Bearer {SPLUNK_TOKEN}"
    return headers


def _use_sample_data() -> bool:
    return not SPLUNK_BASE_URL or not SPLUNK_TOKEN


def using_sample_data() -> bool:
    """Public helper to tell whether the client will use sample data.

    Returns True if either `SPLUNK_BASE_URL` or `SPLUNK_TOKEN` is not set.
    """
    return _use_sample_data()


def _sample_alert() -> dict:
    return {
        "id": "alert-001",
        "title": "Brute Force Login Attempts Detected",
        "source": "Splunk Alert",
        "timestamp": "2026-06-13T08:42:00Z",
        "description": "Multiple failed login attempts detected from a single external IP.",
        "source_ip": "198.51.100.42",
        "severity": "High"
    }


def _sample_logs() -> list[dict]:
    return [
        {
            "timestamp": "2026-06-13T08:40:01Z",
            "user": "admin",
            "source_ip": "198.51.100.42",
            "event": "Failed login",
            "geo": "India",
            "status": "failure",
            "count": 7,
        }
    ]


def _create_search_job(search: str) -> str:
    url = f"{SPLUNK_BASE_URL}/services/search/jobs"
    data = {"search": search, "output_mode": "json"}
    with httpx.Client(verify=SPLUNK_VERIFY_SSL) as client:
        response = client.post(url, headers=_headers(), data=data)
        response.raise_for_status()
        return response.json()["sid"]


def _wait_for_job(sid: str, timeout: int = 30) -> None:
    url = f"{SPLUNK_BASE_URL}/services/search/jobs/{sid}"
    with httpx.Client(verify=SPLUNK_VERIFY_SSL) as client:
        for _ in range(timeout):
            response = client.get(url, headers=_headers(), params={"output_mode": "json"})
            response.raise_for_status()
            content = response.json()
            if content["entry"][0]["content"].get("isDone"):
                return
            time.sleep(1)
    raise RuntimeError("Splunk search job did not complete in time")


def _fetch_results(sid: str, count: int = 100) -> list[dict]:
    url = f"{SPLUNK_BASE_URL}/services/search/jobs/{sid}/results"
    params = {"output_mode": "json", "count": count}
    with httpx.Client(verify=SPLUNK_VERIFY_SSL) as client:
        response = client.get(url, headers=_headers(), params=params)
        response.raise_for_status()
        return response.json().get("results", [])


def fetch_alert(alert_id: str) -> dict:
    if _use_sample_data():
        return _sample_alert()

    query = f'search index=* alert_id="{alert_id}" | head 1'
    sid = _create_search_job(query)
    _wait_for_job(sid)
    results = _fetch_results(sid, count=1)
    if not results:
        return _sample_alert()

    event = results[0]
    return {
        "id": alert_id,
        "title": event.get("alert_name", "Splunk Alert"),
        "source": "Splunk Alert",
        "timestamp": event.get("_time", ""),
        "description": event.get("_raw", ""),
        "source_ip": event.get("src_ip") or event.get("source_ip"),
        "severity": event.get("severity", "Medium"),
    }


def search_logs(query: str) -> list[dict]:
    if _use_sample_data():
        return _sample_logs()

    search_query = query.strip()
    if not search_query.lower().startswith("search"):
        search_query = f"search {search_query}"

    sid = _create_search_job(search_query)
    _wait_for_job(sid)
    return _fetch_results(sid, count=100)
