from unittest import result
from dotenv import load_dotenv
load_dotenv()
import os
from browser_use import Agent,Browser,ChatGoogle
import asyncio
os.environ["ANONYMIZED_TELEMETRY"] = "false"

async def run_browser_task(task: str) -> str:
    """
    Run a general-purpose agent in a visible browser.
    - `task`: the user prompt describing what to do.
    """
    # Launch browser (visible)
    browser = Browser(headless=False, window_size={'width': 1000, 'height': 700},keep_alive=True)

    # Agent with LLM to interpret user instructions
    agent = Agent(task=task, browser=browser, llm=ChatGoogle(model="gemini-2.0-flash"))
    # Run the agent
    result = await agent.run()
    return str(result)
  


