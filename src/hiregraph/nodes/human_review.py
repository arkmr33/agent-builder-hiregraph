from langgraph.types import interrupt

def human_review(state):
    print("\n========== wait for approval ==========\n")
    result = interrupt({
            "message": "approval needed",
            "request": "Please approvev to proceed",
        })
    print("interrupt result:", result)

    return {
        "human_approved": result
    }