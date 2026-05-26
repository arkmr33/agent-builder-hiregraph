from langchain.tools import tool

@tool
def tavily_search(query: str):
    """
    Search public web data.
    """

    return f"Search results for {query}"