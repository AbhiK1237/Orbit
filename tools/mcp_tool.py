# mcp_client/mcp_tool.py
import asyncio
from camel.toolkits.mcp_toolkit import MCPToolkit

async def load_mcp_tools(config_path="mcp_client/config/mcp_config.json"):
    async with MCPToolkit(config_path=config_path) as toolkit:
        tools = toolkit.get_tools()
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
        return safe_tools

def get_mcp_tools():
    return asyncio.run(load_mcp_tools())
