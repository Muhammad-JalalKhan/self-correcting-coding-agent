import os
import json
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from graph import graph # Ensure your graph is imported
from dotenv import load_dotenv
import json
from fastapi.responses import StreamingResponse


load_dotenv()

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows the handshake to happen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- THE FIX ENDS HERE ---

from pydantic import BaseModel

class AgentRequest(BaseModel):
    # Make sure these names are EXACTLY what the frontend sends
    prompt: str
    thread_id: str = "default_thread" # Setting a default makes it optional
@app.post("/run-agent")
async def run_agent(request: AgentRequest):
    async def event_generator():
        config = {"configurable": {"thread_id": str(uuid.uuid4())}}
        inputs = {"messages": [("user", request.prompt)]}
        
        # We use graph.stream to get updates as they happen
        for output in graph.stream(inputs, config=config, stream_mode="updates"):
            # 'output' looks like {'programmer': {...}} or {'terminal': {...}}
            yield f"data: {json.dumps(output)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    # Use 0.0.0.0 to make it accessible on your network IP
    uvicorn.run(app, host="0.0.0.0", port=8000)