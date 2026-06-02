from langchain_core.messages import HumanMessage
from src.hiregraph.llm import llm
from src.hiregraph.tools.search import tavily_search
from src.hiregraph.tools.github_lookup import github_lookup
import re


tools = [tavily_search, github_lookup]

llm_with_tools = llm.bind_tools(tools)



def extract_github_username(text: str):
    match = re.search(r"github\.com/([a-zA-Z0-9_-]+)", text)
    return match.group(1) if match else None


def research_agent(state):

    messages = state.get("messages", [])

    # First entry
    if not messages:

        github_username = extract_github_username(state["resume_text"])

        prompt = f"""
        Research this candidate thoroughly.

        Extracted GitHub username (USE THIS EXACTLY):
        {github_username}

        You MUST use the following tools:
        {tools}
        
        IMPORTANT:
        Do not skip any tool.
        Use each of the tools only ONCE.
        use extracted username above to lookup GitHub profile.
        Do NOT guess names like "john Doe".
        produce a FINAL research summary.
        Do not endlessly call tools.
        """

        messages = [HumanMessage(content=prompt)]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }