from typing import TypedDict, Annotated
import operator


class HireGraphState(TypedDict):
    resume_text: str
    jd_text: str

    seniority: str
    required_skills: list[str]

    completed_skill_reviews: Annotated[list, operator.add]

    scores: Annotated[list, operator.add]

    final_score: Annotated[float, lambda old, new: new] 
    
    recommendation: Annotated[str, lambda old, new: new] 

    draft_email: Annotated[str, lambda old, new: new]
    critique_attempts: int

    parser_error: str
    human_approved: bool

    email_sent: Annotated[bool, lambda old, new: new]
    ats_updated: Annotated[bool, lambda old, new: new]

    compensation_log: list[str]

    audit_trail: Annotated[list, operator.add]

    messages: Annotated[list, operator.add]