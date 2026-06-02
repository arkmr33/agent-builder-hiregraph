from src.hiregraph.llm import llm
from langgraph.types import Command
from typing import Literal

def draft_email(state):
    prompt = f"""
    Write to candidate email based on below recommendation.

    Recommendation:
    {state["recommendation"]}
    """

    result = llm.invoke(prompt)

    return {
        "draft_email": result.content
    }

def critic_loop(
    state
) -> Command[
    Literal[
        "draft_email",
        "send_email_and_update_ats",
        "human_review"
    ]
]:
    attempts = state["critique_attempts"]

    if attempts >= 3:
        return Command(
            goto="human_review"
        )

    if len(state["draft_email"]) < 50:
        return Command(
            goto="draft_email",
            update={
                "critique_attempts": attempts + 1
            }
        )

    return Command(
        goto="send_email_and_update_ats"
    )


def send_email_and_update_ats(state):
    should_fail = state.get("should_fail_email", False)

    if should_fail:
        raise Exception("ATS update failed")

    return {
    "email_sent": True,
    "ats_updated": True,
    "audit_trail": [
        {"node": "send_email_and_update_ats"}
    ]
}



# def send_email_and_update_ats(state):
#     should_fail = state.get("should_fail_email", False)

#     if should_fail:
#         raise Exception("ATS update failed")

#     return Command(
#         goto="finalize",
#         update={
#             "email_sent": True,
#             "ats_updated": True,
#             "audit_trail": state.get("audit_trail", []) + [
#                 {"node": "send_email_and_update_ats"}
#             ]
#         }
#     )