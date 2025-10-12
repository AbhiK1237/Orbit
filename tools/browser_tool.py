import asyncio
from camel.toolkits import FunctionTool
from agents.browser_agent import run_browser_task

async def _browser_func(task: str) -> str:
    """
    Handles tasks requiring browser navigation and automation.
    """
    return await run_browser_task(task)

def browser_tool():
    return FunctionTool(_browser_func)