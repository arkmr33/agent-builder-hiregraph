from pathlib import Path
from langgraph.types import Command
from hiregraph.graph import build_graph
import uuid

def load_file(path):
    return Path(path).read_text()


def test_graph_builds():
    graph = build_graph()

    assert graph is not None

    print("Graph built successfully.")
    print("starting graph execution...")




    thread_id = str(uuid.uuid4())
    config = {
        "configurable": {
            "thread_id":thread_id
        }
    }

    # ---------------- INPUT DATA ----------------
    resume = load_file(r"D:\Machine_learning\Deeplearning\aiml_tutorials\azure_ai\python_rag\agentbuildercourse_satvik\hire_graph\sample_data\resumes\resume_eitan.md")
    jd = load_file(r"D:\Machine_learning\Deeplearning\aiml_tutorials\azure_ai\python_rag\agentbuildercourse_satvik\hire_graph\sample_data\jds\jd_senior_backend.md")


    initial_state = {
        "resume_text": resume,
        "jd_text": jd,

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
        "messages": [],
        "repair_attempts": 0,
        "parser_error": "",
    }

    # ---------------- RUN GRAPH ----------------
    # result = graph.stream(initial_state, config=config)
    result = graph.invoke(initial_state, config=config)

    # ---------------- HANDLE HUMAN INTERRUPT ----------------
    while True:
        if isinstance(result, dict) and "__interrupt__" in str(result):

            approved = input("Approve candidate? (yes/no): ").lower() == "yes"

            result = graph.invoke(
                Command(resume=approved),
                config=config
            )

        else:
            break
        
        # result = graph.stream(
        #     Command(resume="approved"),
        #     config=config
        # )

    # ---------------- OUTPUT ----------------

    # final_state = None

    # for event in result:
        # print(event)  # optional debugging
        # final_state = event
        # print(final_state)  # optional debugging

    # ---------------- OUTPUT ----------------
    print("\n========== FINAL RESULT ==========\n")
    print(" number of reattempts:", result["repair_attempts"])

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

    # print(result)

    # # ---------------- SAVE GRAPH IMAGE ----------------
    # Path("graph_out_teste2e").mkdir(exist_ok=True)

    # output_path = Path(__file__).parent / "graph.png"

    # png = graph.get_graph().draw_mermaid_png(
    #     max_retries=5,
    #     retry_delay=2.0,
    # )

    # with open(output_path, "wb") as f:
    #     f.write(png)

    # print(f"Saved to {output_path}")

test_graph_builds()