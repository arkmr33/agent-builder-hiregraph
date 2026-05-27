#from langchain.tools import tool
from langchain_core.tools import tool

@tool
def github_lookup(username: str):
    """
    Lookup GitHub profile.
    """

    return f"GitHub profile for {username}"