import asyncio
from dotenv import load_dotenv
load_dotenv()
from camel.toolkits.mcp_toolkit import MCPToolkit
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import GeminiConfig


model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_5_PRO,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)

async def main():
     async with MCPToolkit(config_path="config/mcp_config.json") as toolkit:
      agent = ChatAgent(model=model, tools=toolkit.get_tools())
      response = await agent.astep("Add a page titled 'Mcp test' to page 'Notes'")
      print(response.msgs[0].content)

asyncio.run(main())