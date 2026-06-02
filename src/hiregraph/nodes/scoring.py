from src.hiregraph.llm import llm
from src.hiregraph.schemas import ScoreOutput

structured_llm = llm.with_structured_output(ScoreOutput)


def experience_scorer(state):

    prompt = f"""
    Return a number from 1 to 10 based on strict rubric:
    
    Scoring guide:
    1-3: weak candidate, missing skills, irrelevant experience
    4-6: partial match, some gaps
    7-8: good match but missing depth or scale
    9-10: exceptional top-tier candidate with proven production impact

    Do NOT default high. If unsure, score low.

    Resume:
    {state["resume_text"]}

    Job Description:
    {state["jd_text"]}

    Return ONLY a number.
    """

    result = structured_llm.invoke(prompt)

    score = result.score

    return {
        "scores": [score],
        "audit_trail": [
            {"node": "experience_scorer", "score": score}
        ]
    }



def education_scorer(state):

    prompt = f"""
    You are an expert hiring evaluator.

    Evaluate the candidate's EDUCATION fit for the role.

    Consider:
    - degree relevance
    - university quality
    - certifications
    - academic background
    - relevance to the JD

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

    result = structured_llm.invoke(prompt)

    score = result.score

    return {
        "scores": [score],
        "audit_trail": [
            {
                "node": "education_scorer",
                "score": score
            }
        ]
    }



def signal_scorer(state):

    prompt = f"""
    You are an expert hiring evaluator.

    Evaluate the candidate's PUBLIC / PROFESSIONAL SIGNALS.

    Consider:
    - GitHub activity
    - open source work
    - publications
    - leadership
    - certifications
    - technical blogging
    - speaking engagements
    - community participation
    - portfolio quality

    Resume:
    {state["resume_text"]}

    Job Description:
    {state["jd_text"]}

    Be extremely strict.

    Return a number from 1 to 10 based on strict rubric:
    
    Scoring guide:
    1-3: weak candidate, missing skills, irrelevant experience
    4-6: partial match, some gaps
    7-8: good match but missing depth or scale
    9-10: exceptional top-tier candidate with proven production impact

    Do NOT default high. If unsure, score low.
    """

    result = structured_llm.invoke(prompt)

    score = result.score
   

    return {
        "scores": [score],
        "audit_trail": [
            {
                "node": "signal_scorer",
                "score": score
            }
        ]
    }

# def experience_scorer(state):
#     return {
#         "scores": [7],
#         "audit_trail": state.get("audit_trail", []) + [
#             {"node": "experience_scorer"}
#         ]
#     }


# def education_scorer(state):
#     return {
#         "scores": [8],
#         "audit_trail": state.get("audit_trail", []) + [
#             {"node": "education_scorer"}
#         ]
#     }


# def signal_scorer(state):
#     return {
#         "scores": [6],
#         "audit_trail": state.get("audit_trail", []) + [
#             {"node": "signal_scorer"}
#         ]
#     }



def aggregate_scores(state):
    scores = state.get("scores", [])

    if not scores:
        return {"final_score": 0}

    avg = sum(scores) / len(scores)

    return {
    "final_score": avg,
    "audit_trail": [
        {"node": "aggregate_scores"}
    ]
}