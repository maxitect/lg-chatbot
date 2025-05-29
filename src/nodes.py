from langchain.chat_models import init_chat_model
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

from models import State
from tools import tools

load_dotenv()
llm = init_chat_model("openai:gpt-4.1-nano")

tool_node = ToolNode(tools)

llm_with_tools = llm.bind_tools(tools)


def chatbot_node(state: State):
    message = llm_with_tools.invoke(state["messages"])
    assert (len(message.tool_calls) <= 1)
    return {"messages": [message]}
