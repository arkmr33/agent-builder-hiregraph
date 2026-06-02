
from langgraph.prebuilt import ToolNode
from src.hiregraph.tools.github_lookup import github_lookup
from src.hiregraph.tools.search import tavily_search
from langchain_core.messages import ToolMessage


tool_node = ToolNode([
    tavily_search,
    github_lookup
])



def debug_tool_node(state):
    print("\n================ TOOL NODE EXECUTING ================\n")

    print("Incoming tool request keys:", list(state.keys()))

    result = tool_node.invoke(state)

    print("\n================ RAW TOOL RESULT ================\n")
    print(result)

    # Extract readable tool outputs
    messages = result.get("messages", [])

    print("\n================ TOOL OUTPUTS (CLEAN) ================\n")

    for msg in messages:
        if isinstance(msg, ToolMessage):
            print(f"\nTool: {msg.name}")
            print(f"Content:\n{msg.content}")
            print("-" * 60)

    return result


