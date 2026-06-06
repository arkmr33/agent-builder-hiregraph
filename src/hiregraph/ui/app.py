# import streamlit as st

# st.title("HireGraph")

# resume = st.text_area(
#     "Paste Resume"
# )

# jd = st.text_area(
#     "Paste Job Description"
# )

# if st.button("Run"):
    

import streamlit as st
import requests

st.set_page_config(page_title="HireGraph", layout="wide")

st.title("HireGraph - Smart Hiring Assistant")

st.write("Upload Resume and Job Description to evaluate candidate")

# ---------------- INPUT ----------------
resume = st.file_uploader("Upload Resume (.txt / .md / .docx)", type=["txt", "md", "docx"])
jd = st.file_uploader("Upload Job Description (.txt / .md)", type=["txt", "md"])

# ---------------- RUN ----------------
if st.button("Run HireGraph"):
    st.success("Processing candidate...")
    if not resume or not jd:
        st.error("Please upload both Resume and JD")
    else:
        with st.spinner("Running HireGraph pipeline..."):

            files = {
                "resume": resume,
                "jd": jd
            }

            try:
                response = requests.post(
                    "http://localhost:8000/run",
                    files=files
                )

                if response.status_code == 200:
                    result = response.json()

                    st.success("Evaluation Complete")

                    # ---------------- RESULTS ----------------
                    st.subheader("📊 Final Result")

                    st.metric("Final Score", result.get("final_score", "N/A"))
                    st.write("**Recommendation:**", result.get("recommendation"))
                    st.write("**Human Approved:**", result.get("human_approved"))
                    st.write("**Email Sent:**", result.get("email_sent"))
                    st.write("**ATS Updated:**", result.get("ats_updated"))

                    # ---------------- SKILLS ----------------
                    st.subheader("🧠 Skill Reviews")
                    for item in result.get("completed_skill_reviews", []):
                        st.write(item)

                    # ---------------- SCORES ----------------
                    st.subheader("📈 Scores")
                    st.write(result.get("scores", []))

                    # ---------------- EMAIL ----------------
                    st.subheader("✉️ Draft Email")
                    st.text_area(
                        "Email",
                        result.get("draft_email", ""),
                        height=250
                    )

                    # ---------------- AUDIT ----------------
                    st.subheader("🧾 Audit Trail")
                    st.json(result.get("audit_trail", []))

                else:
                    st.error("API Error")
                    st.text(response.text)

            except Exception as e:
                st.error(f"Request failed: {str(e)}")