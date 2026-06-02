from src.hiregraph.llm import llm
from src.hiregraph.schemas import SeniorityOutput

structured_llm = llm.with_structured_output(
    SeniorityOutput
)

def classify_seniority(state):
    prompt = f"""
    Resume:
    {state["resume_text"]}

    Determine candidate seniority.
    """

    result = structured_llm.invoke(prompt)

    return {
        "seniority": result.level
    }