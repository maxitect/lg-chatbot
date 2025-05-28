from langchain.chat_models import init_chat_model
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

from models import State
from tools import tools

load_dotenv()

tool_node = ToolNode(tools)

llm = init_chat_model("openai:gpt-4.1-nano")
llm_with_tools = llm.bind_tools(tools)


def chatbot_node(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


def human_assistance_node(state: State):
    return state
