from typing import List
from pydantic import BaseModel

class Incident(BaseModel):
    id: str
    title: str
    severity: str
    source: str
    timestamp: str
    status: str
    summary: str
    affected_asset: str

class InvestigationRequest(BaseModel):
    alert_id: str
    query: str | None = None

class InvestigationResponse(BaseModel):
    incident_summary: str
    severity_score: int
    business_impact: str
    probable_root_cause: str
    confidence: float
    mitre_techniques: List[str]
    recommended_actions: List[str]

class ReportRequest(BaseModel):
    incident_id: str

class ReportResponse(BaseModel):
    report_url: str
    message: str

class RecommendationRequest(BaseModel):
    incident_id: str

class RecommendationResponse(BaseModel):
    actions: List[str]

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    response: str
