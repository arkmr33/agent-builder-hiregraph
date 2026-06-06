def advance(state):
    return {
        "audit_trail": [
            {
                "node": "advance"
            }
        ]
    }


def reject(state):
    return {
        "audit_trail": [
            {
                "node": "reject"
            }
        ]
    }




def borderline(state):
    return {
        "audit_trail": [
            {
                "node": "borderline"
            }
        ]
    }



