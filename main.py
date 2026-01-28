from graph import graph
from langchain_core.messages import HumanMessage

def run_agent(user_prompt):
    inputs = {"messages": [HumanMessage(content=user_prompt)]}
    config = {"configurable": {"thread_id": "prod_test_1"}}
    
    print("--- 🤖 Starting Agentic Loop ---")
    # Using invoke to avoid OpenRouter streaming issue
    result = graph.invoke(inputs, config=config)
    
    print("\n--- ✅ FINAL RESULT ---")
    print(result["messages"][-1].content)

if __name__ == "__main__":
    task = "Sum this list ['1', '2', '3'] without converting to int first, catch the error, and fix it."
    run_agent(task)