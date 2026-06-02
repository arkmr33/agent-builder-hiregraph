from langgraph.types import Command
from typing import Literal


# def ats_result_router(
#     state
# ) -> Command[
#     Literal[
#         "finalize",
#         "compensate"
#     ]
# ]:
#     if state.get("ats_updated"):
#         return Command(
#             goto="finalize"
#         )

#     return Command(
#         goto="compensate"
#     )

def ats_result_router(state) -> Literal["finalize", "compensate"]:
    if state.get("ats_updated"):
        return "finalize"
    return "compensate"