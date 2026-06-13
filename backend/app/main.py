from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from .models import (
    Incident,
    InvestigationRequest,
    InvestigationResponse,
    ReportRequest,
    ReportResponse,
    RecommendationRequest,
    RecommendationResponse,
    ChatRequest,
    ChatResponse,
)
from .splunk_client import fetch_alert, search_logs, using_sample_data
from .ai_agents import summarize_incident, generate_report, recommend_actions, chat_response

app = FastAPI(
    title="SentinelAI",
    description="Autonomous security investigation and response platform built on Splunk.",
    version="0.1.0",
)

# Enable CORS for the frontend dev server (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = Path(__file__).resolve().parents[2] / "sample-data"
INCIDENTS = [
    {
        "id": "incident-001",
        "title": "Suspicious failed logins",
        "severity": "High",
        "source": "Splunk Alert",
        "timestamp": "2026-06-13T08:42:00Z",
        "status": "Open",
        "summary": "Multiple failed authentication attempts were detected from an external IP address.",
        "affected_asset": "Domain Controller"
    }
]


@app.get("/incidents", response_model=list[Incident])
def list_incidents():
    return INCIDENTS


@app.get("/incident/{incident_id}", response_model=Incident)
def get_incident(incident_id: str):
    for incident in INCIDENTS:
        if incident["id"] == incident_id:
            return incident
    raise HTTPException(status_code=404, detail="Incident not found")


@app.post("/investigate", response_model=InvestigationResponse)
def investigate(request: InvestigationRequest):
    alert = fetch_alert(request.alert_id)
    logs = search_logs(request.query or "")
    summary = summarize_incident(alert, logs)
    return InvestigationResponse(**summary)


@app.post("/generate-report", response_model=ReportResponse)
def create_report(request: ReportRequest):
    report = generate_report(request.incident_id)
    return ReportResponse(**report)


@app.post("/recommend-actions", response_model=RecommendationResponse)
def action_recommendation(request: RecommendationRequest):
    return RecommendationResponse(actions=recommend_actions(request.incident_id))


@app.post("/chat", response_model=ChatResponse)
def investigative_chat(request: ChatRequest):
    return ChatResponse(response=chat_response(request.user_message))


@app.get("/splunk-status")
def splunk_status():
    """Return whether the backend will use sample data (True) or attempt live Splunk queries (False)."""
    return {"using_sample_data": using_sample_data()}
