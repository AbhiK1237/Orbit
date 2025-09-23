import asyncio
from camel.toolkits import FunctionTool
from agents.browser_agent import run_browser_task

def _browser_func(task: str) -> str:
    """
    Handles tasks requiring browser navigation and automation.
    """
    return asyncio.run(run_browser_task(task))

def browser_tool():
    return FunctionTool(_browser_func)