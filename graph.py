from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from state import AgentState
from llm import get_model
from tools import execute_and_fix_code # <--- EXACT MATCH

# 1. Setup
tools = [execute_and_fix_code]
model = get_model().bind_tools(tools)

# 2. Nodes
def call_ai(state):
    response = model.invoke(state["messages"])
    return {"messages": [response]}

# 3. Graph Construction
builder = StateGraph(AgentState)
builder.add_node("programmer", call_ai)
builder.add_node("terminal", ToolNode(tools))

builder.set_entry_point("programmer")

def router(state):
    if state["messages"][-1].tool_calls:
        return "terminal"
    return END

builder.add_conditional_edges("programmer", router)
builder.add_edge("terminal", "programmer")

# 4. Compile with Memory
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)