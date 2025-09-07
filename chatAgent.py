from dotenv import load_dotenv
load_dotenv()
import os
# load_dotenv(dotenv_path="./.env")  # explicitly load
# print(os.getenv("GEMINI_API_KEY"))
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import GeminiConfig
from camel.agents import ChatAgent
from camel.toolkits import FunctionTool,SearchToolkit,TwitterToolkit
from camel.toolkits.twitter_toolkit import create_tweet, delete_tweet, get_my_user_profile, get_user_by_username


twitter_tools = [
    FunctionTool(create_tweet),
    FunctionTool(delete_tweet),
    FunctionTool(get_my_user_profile),
    FunctionTool(get_user_by_username),
]

print(create_tweet("hello world from api"))
model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_5_PRO,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)

def calculate_sum(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

add_tool = FunctionTool(calculate_sum)
google_tool = FunctionTool(SearchToolkit().search_google)
agent = ChatAgent(
    system_message="You are a helpful assistant.",
    model=model,
    tools=[add_tool, google_tool, *twitter_tools]
)

# res = agent.step("create a tweet saying hello world")
# print(res.msgs[0].content)