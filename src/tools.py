from langchain_tavily import TavilySearch

search = TavilySearch(max_results=2)
tools = [search]
search.invoke("What's a 'node' in LangGraph?")
