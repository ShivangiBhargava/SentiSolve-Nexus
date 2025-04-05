from fastapi import FastAPI, Request
from pydantic import BaseModel
from agents.summarizer_agent import summarize_ticket
from agents.root_cause_classifier import classify_root_cause
from agents.resolution_recommender import recommend_resolution
from agents.router import route_ticket
from agents.eta_predictor import predict_eta

app = FastAPI()

class TicketRequest(BaseModel):
    ticket_text: str

@app.post("/analyze")
def analyze_ticket(req: TicketRequest):
    summary = summarize_ticket(req.ticket_text)
    root_cause = classify_root_cause(summary)
    resolution, score = recommend_resolution(summary)
    team = route_ticket(root_cause)
    eta = predict_eta({"length": len(req.ticket_text), "issue_type": 1})

    return {
        "summary": summary,
        "root_cause": root_cause,
        "recommended_resolution": resolution,
        "similarity_score": round(score * 100, 2),
        "routed_team": team,
        "eta_hours": eta
    }
