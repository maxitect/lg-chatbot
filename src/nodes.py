from langchain.chat_models import init_chat_model

from models import State
from tools import tools

llm = init_chat_model("openai:gpt-4.1-nano")
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}
