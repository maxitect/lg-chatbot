from langchain_tavily import TavilySearch
from langgraph.types import interrupt
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()


@tool
def human_assistance(query: str) -> str:
    """Request assistance from a human."""
    human_response = interrupt({"query": query})
    return human_response["data"]


search = TavilySearch(max_results=2)
tools = [search, human_assistance]
