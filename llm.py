import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load the .env file
load_dotenv()

def get_model():
    return ChatOpenAI(
        model="xiaomi/mimo-v2-flash:free", # or your devstral model
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        streaming=False,  # <--- ADD THIS LINE FOR EXTRA SAFETY
        # ... other settigs ...
    )