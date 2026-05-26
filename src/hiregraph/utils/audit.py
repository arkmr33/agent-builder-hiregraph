from datetime import datetime


def audit_event(
    state,
    node_name
):
    logs = state.get(
        "audit_trail",
        []
    )

    logs.append(
        {
            "node": node_name,
            "timestamp": str(
                datetime.utcnow()
            )
        }
    )

    return logs