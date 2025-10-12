# import asyncio
# from camel.agents import ChatAgent
# from camel.models import ModelFactory
# from camel.types import ModelPlatformType, ModelType
# from camel.configs import GeminiConfig

# from tools.browser_tool import browser_tool
# from tools.document_tool import document_tool
# from tools.mcp_tool import get_mcp_tools

# async def main():
#     model = ModelFactory.create(
#         model_platform=ModelPlatformType.GEMINI,
#         model_type=ModelType.GEMINI_2_5_PRO,
#         model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
#     )

#     tools = [browser_tool(), document_tool()] + await get_mcp_tools()

#     agent = ChatAgent(
#         system_message="You are a helpful assistant that can use various tools to assist the user.",
#         model=model, 
#         tools=tools
#         )

#     print("🤖 Orchestrator ready. Type your query (or 'exit' to quit).")
#     while True:
#         query = input("\n>> ")
#         if query.lower() in ["exit", "quit"]:
#             break
#         response = await agent.astep(query)
#         print("\n=== Response ===")
#         print(response.msgs[0].content)

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import GeminiConfig
from camel.toolkits import MCPToolkit
from tools.browser_tool import browser_tool
from tools.document_tool import document_tool

async def main():
    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_2_5_PRO,
        model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
    )
    
    # Create MCP toolkit and keep connection alive
    toolkit = MCPToolkit(config_path="mcp_client/config/mcp_config.json")
    
    try:
        # Connect to MCP servers
        await toolkit.connect()
        
        # Get all MCP tools
        all_mcp_tools = toolkit.get_tools()
        
        # Filter out problematic tools
        excluded_tools = {
            "notion-update-page",
            "notion-create-database",
            "notion-update-database",
            "notion-create-pages",
            "notion-create-comment",
        }
        
        safe_mcp_tools = [
            tool for tool in all_mcp_tools 
            if tool.func.__name__ not in excluded_tools
        ]
        
        print(f"✅ Loaded {len(safe_mcp_tools)} MCP tools")
        
        # Combine all tools
        tools = [browser_tool(), document_tool()] + safe_mcp_tools
        
        # Create agent
        agent = ChatAgent(
            system_message="You are a helpful assistant that can use various tools to assist the user.",
            model=model,
            tools=tools
        )
        
        print("🤖 Orchestrator ready. Type your query (or 'exit' to quit).")
        
        # Main loop - connection stays alive here
        while True:
            query = input("\n>> ")
            if query.lower() in ["exit", "quit"]:
                break
            
            try:
                response = await agent.astep(query)
                print("\n=== Response ===")
                print(response.msgs[0].content)
            except Exception as e:
                print(f"\n❌ Error: {e}")
    
    finally:
        # Clean up MCP connection
        print("\n🔌 Disconnecting MCP servers...")
        await toolkit.disconnect()
        print("👋 Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())