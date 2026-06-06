from src.hiregraph.llm import llm
from src.hiregraph.schemas import SkillPlan

from langgraph.types import Command

planner = llm.with_structured_output(
    SkillPlan
)

def plan_required_skills(state):
    prompt = f"""
    Job description:
    {state["jd_text"]}

    Extract the top 3 required skills from the given job description.
    """

    result = planner.invoke(prompt)

    return {
        "required_skills": result.required_skills
    }




def wait_for_all(state):

    expected = len(state.get("required_skills", [])) + 3

    current = len(state.get("scores", []))

    print(f"WAITING: {current}/{expected}")

    if current < expected:
        return Command(goto="wait_for_all")

    return Command(goto="aggregate_scores")