import asyncio
from dotenv import load_dotenv
load_dotenv()
from camel.toolkits.mcp_toolkit import MCPToolkit
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import GeminiConfig,ChatGPTConfig


model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_5_PRO,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)


async def main():
     async with MCPToolkit(config_path="config/mcp_config.json") as toolkit:
      tools = toolkit.get_tools()
      # print("Available tools:", [t.func.__name__ for t in tools])
      safe_tools = [
            t for t in tools
            if t.func.__name__ not in [
                "notion-update-page",
                "notion-create-database",
                "notion-update-database",
                "notion-create-pages",
                "notion-create-comment",
            ]
        ]
      agent = ChatAgent(model=model, tools=safe_tools)
      response = await agent.astep("list all the tools of")
      print(response.msgs[0].content)

asyncio.run(main())