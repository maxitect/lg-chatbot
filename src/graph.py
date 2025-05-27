import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START
from IPython.display import Image, display

from models import State
from nodes import chatbot

graph_builder = StateGraph(State)

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()

print(graph.get_graph().draw_ascii())
