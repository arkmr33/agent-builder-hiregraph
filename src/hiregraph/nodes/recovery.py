from langgraph.types import Command
from typing import Literal

def parser_node(state):
    try:
        value = int("bad")
    except Exception as e:
        return {
            "parser_error": str(e)
        }

def parser_router(
    state
) -> Command[
    Literal[
        "repair_node",
        "continue_node"
    ]
]:
    if state["parser_error"]:
        return Command(
            goto="repair_node"
        )

    return Command(
        goto="continue_node"
    )

def repair_node(state):
    return {
        "parser_error": ""
    }