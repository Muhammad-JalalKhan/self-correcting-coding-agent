from langchain_core.tools import tool
from pydantic import BaseModel, Field
from executor import run_code_in_cloud


class CodeInput(BaseModel):
    filename: str = Field(description="Name of the file to test")
    code: str = Field(description="The complete python code")

@tool(args_schema=CodeInput)
def execute_and_fix_code(filename: str, code: str):
    """Saves and runs code in E2B Cloud Sandbox to check for errors."""
    print(f"\n📡 [Agent] Testing '{filename}' in E2B Cloud...")
    
    result = run_code_in_cloud(code)
    
    if result["status"] == "success":
        return f"SUCCESS: Output:\n{result['output']}"
    else:
        return f"ERROR in {filename}: {result['message']}\nTraceback:\n{result.get('traceback')}"