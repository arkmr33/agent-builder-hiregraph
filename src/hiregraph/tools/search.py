#from langchain.tools import tool
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilySearch(
    max_results=5,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def tavily_search(query:str):
    """
    Search public web data using the query string.
    """
    
    results = tavily.invoke({"query": query})

    summaries = []

    items = results.get("results", [])

    for r in items:
        title = r.get("title", "")
        content = r.get("content", "")

        summaries.append(f"- {title}: {content}")

    return {
        "search_summary": "\n".join(summaries)
    }



# @tool
# def tavily_search(query: str):
#     """
#     Search public web data.
#     """

#     return f"Search results for {query}"