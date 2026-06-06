from langgraph.types import interrupt

def human_review(state):
    print("\n========== wait for approval ==========\n")
    result = interrupt(
        {
            "recommendation": state["recommendation"],
            "score": state["final_score"]
        }
    )

    return {
        "human_approved": result
    }