from langgraph.types import interrupt

def human_review(state):
    result = interrupt(
        {
            "recommendation": state["recommendation"],
            "score": state["final_score"]
        }
    )

    return {
        "human_approved": result
    }