from pydantic import BaseModel
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