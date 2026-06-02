from src.hiregraph.llm import llm

def draft_rejection(state):
    response = llm.invoke(
        "Write rejection email."
    )

    return {
        "draft_email": response.content
    }

def log_rejection(state):
    logs = state["audit_trail"]

    logs.append(
        {
            "event": "candidate_rejected"
        }
    )

    return {
    "audit_trail": [
        {
            "event": "candidate_rejected"
        }
    ]
}