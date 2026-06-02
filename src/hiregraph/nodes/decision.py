from langgraph.types import Command
from typing import Literal


def recommendation(
    state
) -> Command[
    Literal[
        "advance",
        "borderline",
        "reject"
    ]
]:
    score = state.get("final_score", 0)

    if score >= 8:
        return Command(
            goto="advance",
            update={
                "recommendation": "advance"
            }
        )

    if score < 5:
        return Command(
            goto="reject",
            update={
                "recommendation": "reject"
            }
        )

    return Command(
        goto="borderline",
        update={
            "recommendation": "borderline"
        }
    )