from fastapi import FastAPI
from fastapi import FastAPI, UploadFile
from hiregraph.graph import build_graph
from langgraph.types import Command


graph = build_graph()

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "HireGraph API Running"
    }





@app.post("/run")
async def run_graph(resume: UploadFile, jd: UploadFile):

    resume_text = (await resume.read()).decode("utf-8", errors="ignore")
    jd_text = (await jd.read()).decode("utf-8", errors="ignore")
    config = {
        "configurable": {
            "thread_id": "testapi-1"
        }
    }

    initial_state = {
        "resume_text": resume_text,
        "jd_text": jd_text,

        "seniority": "",
        "required_skills": [],

        "completed_skill_reviews": [],
        "scores": [],

        "final_score": 0.0,
        "recommendation": "",

        "draft_email": "",
        "critique_attempts": 0,

        "parser_error": "",
        "human_approved": False,

        "email_sent": False,
        "ats_updated": False,

        "compensation_log": [],

        "audit_trail": [],
        "messages": []
    }

    # ---------------- RUN GRAPH ----------------
    # result = graph.stream(initial_state, config=config)
    result = graph.invoke(initial_state, config=config)

    # ---------------- HANDLE HUMAN INTERRUPT ----------------
    while isinstance(result, dict) and "__interrupt__" in str(result):
        print("\nHuman review required. Auto-approving...\n")

        result = graph.invoke(
            Command(resume="approved"),
            config=config
        )
        # result = graph.stream(
        #     Command(resume="approved"),
        #     config=config
        # )

    # ---------------- OUTPUT ----------------

    # final_state = None

    # for event in result:
    #     print(event)  # optional debugging
    #     final_state = event
    #     print(final_state)  # optional debugging

    # ---------------- OUTPUT ----------------
    print("\n========== FINAL RESULT ==========\n")

    print("FINAL SCORE:")
    print(result["final_score"])

    print("\nRECOMMENDATION:")
    print(result["recommendation"])

    print("\nHUMAN APPROVED:")
    print(result["human_approved"])

    print("\nEMAIL SENT:")
    print(result["email_sent"])

    print("\nATS UPDATED:")
    print(result["ats_updated"])

    print("\nSKILL REVIEWS:")
    for review in result["completed_skill_reviews"]:
        print(review)

    print("\nSCORES:")
    print(result["scores"])

    print("\n AUDIT TRAIL COUNT:")
    print(len(result["audit_trail"]))

    print("\n last 10 AUDIT EVENTS:")
    for item in result["audit_trail"][:10]:
        print(item)

    print("\nEMAIL PREVIEW:\n")
    print(result["draft_email"][:500])  # first 100 chars

    return result