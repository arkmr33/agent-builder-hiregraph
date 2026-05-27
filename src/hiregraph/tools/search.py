#from langchain.tools import tool
from langchain_core.tools import tool

@tool
def tavily_search(query: str):
    """
    Search public web data.
    """

    return f"Search results for {query}"