def compensate(state):

    compensations = []

    if state.get("email_sent"):
        compensations.append(
            "Candidate email reverted"
        )

    if state.get("ats_updated"):
        compensations.append(
            "ATS status reverted"
        )

    return {
        "compensation_log": compensations,
        "audit_trail": [
            {
                "node": "compensate",
                "actions": compensations
            }
        ]
    }