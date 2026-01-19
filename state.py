from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    # Keeps the full chat history (Human vs AI)
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # Specifically tracks the code currently in the E2B sandbox
    current_code: str 
    # Tracks how many times we've asked the AI to fix a bug
    retry_count: int