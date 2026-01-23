import os
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv

load_dotenv()

def run_code_in_cloud(code: str):
    api_key = os.getenv("E2B_API_KEY")
    if not api_key:
        return {"status": "error", "message": "E2B_API_KEY missing"}

    try:
        # Create safe sandboxing environment
        with Sandbox(api_key=api_key) as sb:
            execution = sb.run_code(code)
            if execution.error:
                return {
                    "status": "error", 
                    "message": execution.error.value,
                    "traceback": execution.error.traceback
                }
            return {"status": "success", "output": execution.logs.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}