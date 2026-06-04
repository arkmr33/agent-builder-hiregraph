from src.hiregraph.llm import llm
from src.hiregraph.schemas import ScoreOutput
import time
from src.hiregraph.utils.helpers import safe_llm_invoke

structured_llm = llm.with_structured_output(ScoreOutput)

def skill_worker(state):
    skill = state["skill"]

    prompt = f"""
    You are a hiring evaluator.

    Score candidate skill from 1 to 10.

    Skill: {skill}

    Resume:
    {state["resume_text"]}

    Job Description:
    {state["jd_text"]}

    Return a number from 1 to 10 based on strict rubric:
    - 1-3 weak
    - 4-6 average
    - 7-8 strong
    - 9-10 exceptional
    """


    result = safe_llm_invoke(structured_llm, prompt)

    score = result.score
    print("Skill:", skill)
    print("Score:", score)
    return {
        "completed_skill_reviews": [
            {
                "skill": skill,
                "score": score
            }
        ],
        "scores": [score],
        "audit_trail": [
        {
            "node": "skill_worker",
            "skill": skill,
            "score": score
        }
    ]
}

