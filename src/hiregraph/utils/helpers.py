from datetime import datetime

import time
import random
from groq import RateLimitError


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




# def safe_llm_invoke(llm, prompt, retries=5):
#     for i in range(retries):
#         try:
#             return llm.invoke(prompt)
#         except RateLimitError:
#             wait = (2 ** i) + random.uniform(0, 1)
#             print(f"Rate limited. retry {i+1}, sleeping {wait:.2f}s")
#             time.sleep(wait)

#     raise Exception("LLM failed after retries")

def safe_llm_invoke(llm, prompt, retries=5):

    for i in range(retries):

        try:
            return llm.invoke(prompt)

        except RateLimitError:

            # exponential backoff
            wait = min((2 ** i) + random.uniform(0, 1), 30)

            print(
                f"Rate limited. retry {i+1}, "
                f"sleeping {wait:.2f}s"
            )

            time.sleep(wait)

        except Exception as e:

            print(f"LLM error: {e}")

            # optional retry for transient failures
            wait = 2

            time.sleep(wait)

    raise Exception("LLM failed after retries")