from agents.summarizer_agent import summarize_ticket
from agents.vectorizer_agent import embed_ticket
from agents.root_cause_classifier import classify_root_cause
from agents.resolution_recommender import recommend_resolution
from agents.router import route_ticket
from agents.eta_predictor import predict_eta
from agents.feedback_agent import record_feedback

ticket = """
User reports a payment failure on Chrome with 'TLS handshake failed'.
"""

print("📩 New Ticket Received")
summary = summarize_ticket(ticket)
print("Summary:", summary)

root_cause = classify_root_cause(summary)
print("Predicted Root Cause:", root_cause)

resolution, score = recommend_resolution(summary)
print(f"Suggested Resolution ({round(score * 100)}% match):", resolution)

team = route_ticket(root_cause)
print("Routing to:", team)

features = {"length": len(ticket), "issue_type": 1}  # dummy features
eta = predict_eta(features)
print("Estimated Resolution Time:", eta, "hours")

record_feedback(ticket_id="TICKET001", was_successful=True)
