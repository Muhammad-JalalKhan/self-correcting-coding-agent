import os
import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from graph import graph  # Ensure your graph is imported correctly
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# 1. THE SECURITY PASS (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. THE FORM DEFINITION
class AgentRequest(BaseModel):
    prompt: str  # <--- We will use 'prompt' everywhere
    thread_id: str = "default_session"

# 3. THE BRAIN LOGIC
@app.post("/run-agent")
async def run_agent_endpoint(request: AgentRequest):
    async def event_generator():
        try:
            # FIX: Changed request.task to request.prompt to match the class above
            inputs = {"messages": [("user", request.prompt)]}
            config = {"configurable": {"thread_id": request.thread_id}}

            # Use astream for real-time updates
            async for chunk in graph.astream(inputs, config=config, stream_mode="updates"):
                for node, values in chunk.items():
                    # This sends a packet to the website for every step
                    payload = json.dumps({"node": node, "status": "active"})
                    yield f"data: {payload}\n\n"
            
            # Final message
            final_state = graph.get_state(config)
            final_msg = final_state.values["messages"][-1].content
            yield f"data: {json.dumps({'node': 'end', 'output': final_msg})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'node': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)