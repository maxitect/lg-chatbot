from langgraph.types import Command
from graph import graph


def stream_graph_updates(user_input: str):
    config = {"configurable": {"thread_id": "1"}}
    cmd = {"messages": [{"role": "user", "content": user_input}]}

    while True:
        events = graph.stream(cmd, config, stream_mode="updates")

        for event in events:
            if "__interrupt__" in event:
                interrupt_data = event["__interrupt__"]
                human_response = input(f"Human input needed: {interrupt_data} ")
                cmd = Command(resume={"data": human_response})
                break
            else:
                for node_name, node_data in event.items():
                    if "messages" in node_data:
                        node_data["messages"][-1].pretty_print()
        else:
            break


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except (EOFError, KeyboardInterrupt):
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break
