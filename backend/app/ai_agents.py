import os
from typing import List

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def summarize_incident(alert: dict, logs: list[dict]) -> dict:
    return {
        "incident_summary": "AI-generated overview of the alert and related event context.",
        "severity_score": 8,
        "business_impact": "Potential credential exposure and elevated risk to corporate systems.",
        "probable_root_cause": "Brute force authentication attempts from an external IP.",
        "confidence": 0.92,
        "mitre_techniques": ["T1110", "T1078"],
        "recommended_actions": ["Block suspicious IP", "Require password reset", "Monitor for additional login failures"]
    }


def generate_report(incident_id: str) -> dict:
    return {
        "report_url": f"/reports/{incident_id}-executive-report.pdf",
        "message": "Executive report generated successfully."
    }


def recommend_actions(incident_id: str) -> list[str]:
    return [
        "Block the malicious IP address at the firewall",
        "Disable the compromised user account",
        "Review authentication logs for lateral movement",
        "Isolate the affected endpoint"
    ]


def chat_response(prompt: str) -> str:
    if OPENAI_API_KEY:
        return "AI chat response from OpenAI would appear here."
    return "This is a simulated response to your investigation query."
