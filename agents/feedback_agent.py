def record_feedback(ticket_id, was_successful):
    with open("feedback_log.csv", "a") as f:
        f.write(f"{ticket_id},{was_successful}\n")
