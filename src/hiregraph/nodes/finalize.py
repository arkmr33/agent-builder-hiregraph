
from pathlib import Path
from hiregraph.state import HireGraphState
from datetime import datetime


def finalize(state):

    return {
        "audit_trail": [
            {"event": "workflow_completed"}
        ],
        "final_score": state.get("final_score", 0),
        "recommendation": state.get("recommendation", "unknown")
    }



def saver(state: HireGraphState):
    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    out_dir = PROJECT_ROOT / "hire_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report = out_dir / f"report_{ts}.md"

    lines = []

    lines.append("# HireGraph - Candidate Evaluation Report\n")

    lines.append("## Summary")
    lines.append(f"- Final Score: {state.get('final_score', 'N/A')}")
    lines.append(f"- Recommendation: {state.get('recommendation', 'N/A')}")
    lines.append(f"- Human Approved: {state.get('human_approved', False)}")
    lines.append(f"- Email Sent: {state.get('email_sent', False)}")
    lines.append(f"- ATS Updated: {state.get('ats_updated', False)}")
    lines.append("")

    lines.append("## Seniority & Skills")
    lines.append(f"- Seniority: {state.get('seniority', 'N/A')}")
    lines.append(f"- Required Skills: {state.get('required_skills', 'N/A')}")
    lines.append("")

    lines.append("## Skill Reviews")

    for r in state.get("completed_skill_reviews", []):
        lines.append(str(r))

    lines.append("\n## Scores Breakdown")

    for s in state.get("scores", []):
        lines.append(str(s))

    lines.append("\n##  Audit Trail ")

    for a in state.get("audit_trail", []):
        lines.append(str(a))

    lines.append("\n## ✉️ Draft Email\n")
    lines.append(state.get("draft_email", ""))

    # ---------------- WRITE FILE ----------------
    report.write_text("\n".join(lines), encoding="utf-8")

    return state