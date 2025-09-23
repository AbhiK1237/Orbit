import asyncio
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import GeminiConfig

from tools.browser_tool import browser_tool
from tools.document_tool import document_tool
from tools.mcp_tool import get_mcp_tools

async def main():
    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_2_5_PRO,
        model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
    )

    tools = [browser_tool(), document_tool()] + get_mcp_tools()

    agent = ChatAgent(
        system_message="You are a helpful assistant that can use various tools to assist the user.",
        model=model, 
        tools=tools
        )

    print("🤖 Orchestrator ready. Type your query (or 'exit' to quit).")
    while True:
        query = input("\n>> ")
        if query.lower() in ["exit", "quit"]:
            break
        response = await agent.astep(query)
        print("\n=== Response ===")
        print(response.msgs[0].content)

if __name__ == "__main__":
    asyncio.run(main())