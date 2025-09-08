from dotenv import load_dotenv
load_dotenv()
import os
from browser_use import Agent,Browser,ChatGoogle
import asyncio
os.environ["ANONYMIZED_TELEMETRY"] = "false"
browser = Browser(
	headless=False,  # Show browser window
	window_size={'width': 1000, 'height': 700},  # Set window size
)

browser = Browser(
	headless=False,  # Show browser window
	window_size={'width': 1000, 'height': 700},  # Set window size
)

agent = Agent(
	task= input("Enter your task: "),
	browser=browser,
	llm=ChatGoogle(model="gemini-2.0-flash"),
)

async def main():
	await agent.run()
asyncio.run(main())

# from camel.toolkits import BrowserToolkit
# from camel.models import ModelFactory
# from camel.types import ModelPlatformType, ModelType
# from camel.configs import GeminiConfig
# from camel.agents import ChatAgent
# from camel.toolkits import FunctionTool

# gemini_model = ModelFactory.create(
#     model_platform=ModelPlatformType.GEMINI,
#     model_type=ModelType.GEMINI_2_5_PRO,
#     model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
# )

# task_prompt = "Find the main contributions of the paper 'Sparks of AGI' by Microsoft Research."
# start_url = "https://www.google.com"

# browser_toolkit = BrowserToolkit(
#     web_agent_model=gemini_model,
#     planning_agent_model=gemini_model,
# )

# browser_tools = browser_toolkit.get_tools()

# agent = ChatAgent(
#     system_message="You are a helpful assistant.",
#     model=gemini_model,
#     tools=browser_tools
# )
# result = agent.step(f"Please help me with the following task: {task_prompt} Starting from this URL: {start_url}")
# print(result)