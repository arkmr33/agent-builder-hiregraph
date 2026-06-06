from src.hiregraph.llm import llm
from src.hiregraph.schemas import SkillPlan

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
    return {}