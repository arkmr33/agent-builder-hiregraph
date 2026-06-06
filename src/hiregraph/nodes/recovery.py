from langgraph.types import Command
from typing import Literal

def parser_node(state):

    messages = state.get("messages", [])

    if not messages:
        return {
            "parser_error": "No research result generated"
        }

    last = messages[-1]

    if not getattr(last, "content", "").strip():
        return {
            "parser_error": "Empty research summary"
        }

    return {
        "parser_error": ""
    }




# def parser_router(
#     state
# ) -> Command[
#     Literal[
#         "repair_node",
#         "aggregate_scores"
#     ]
# ]:
#     print (f"repair_attempts :{state.get("repair_attempts", 0)}")
#     if state.get("parser_error") and state.get("repair_attempts", 0) < 2:
#         return Command(
#             goto="repair_node"
#         )

#     return Command(
#         goto="aggregate_scores"
#     )

    
def parser_router(state):
    print(f"repair_attempts: {state.get('repair_attempts', 0)}")

    if (
        state.get("parser_error")
        and state.get("repair_attempts", 0) < 2
    ):
        return "repair_node"

    return "wait_for_all"



def repair_node(state):

    return {
        "parser_error": "",
        "repair_attempts": state.get("repair_attempts", 0) + 1,
        "audit_trail": [
            {
                "node": "repair_node",
                "error": state.get("parser_error")
            }
        ]
    }