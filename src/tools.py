from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

search = TavilySearch(max_results=2)
tools = [search]
search.invoke("What's a 'node' in LangGraph?")
