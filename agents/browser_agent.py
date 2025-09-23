from dotenv import load_dotenv
load_dotenv()
import os
from browser_use import Agent,Browser,ChatGoogle
import asyncio
os.environ["ANONYMIZED_TELEMETRY"] = "false"

async def run_browser_task(task: str) -> str:
	browser = Browser(headless=True, window_size={'width': 1000, 'height': 700})
	agent = Agent(task=task, browser=browser, llm=ChatGoogle(model="gemini-2.0-flash"))
	result = await agent.run()
	return str(result)


