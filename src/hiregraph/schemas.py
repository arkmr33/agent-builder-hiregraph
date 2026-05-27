from pydantic import BaseModel,Field
from typing import Literal

class SeniorityOutput(BaseModel):
    level: Literal[
        "junior",
        "mid",
        "senior",
        "executive"
    ]

class SkillPlan(BaseModel):
    required_skills: list[str]




class ScoreOutput(BaseModel):
    score: float = Field(ge=1, le=10)