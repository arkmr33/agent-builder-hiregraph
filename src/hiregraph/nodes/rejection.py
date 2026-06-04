from src.hiregraph.llm import llm
from src.hiregraph.utils.helpers import safe_llm_invoke

def draft_rejection(state):
    response = safe_llm_invoke(
        llm,
        "Write rejection email to candidate."
    )

    return {
        "draft_email": response.content
    }

def rejection_check(state):
    email = state["draft_email"]

    if state.get("human_approved"):
        return "draft_email"
    else:
        return "draft_rejection"


def log_rejection(state):
    
    return {
    "audit_trail": [
        {
            "event": "candidate_rejected"
        }
    ]
}