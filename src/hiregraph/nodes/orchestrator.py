from langgraph.constants import Send

def assign_skill_workers(state):
    return [
        Send(
            "skill_worker",
            {
                "skill": skill,
                "resume_text": state["resume_text"],
                "jd_text": state["jd_text"]
            }
        )
        for skill in state.get("required_skills", [])
    ]