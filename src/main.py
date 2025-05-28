from graph import graph
from langchain_core.messages import ToolMessage

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        print("\033[A\033[K", end="")

        config = {"configurable": {"thread_id": "1"}}

        for event in graph.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            config,
            stream_mode="values",
        ):
            if "messages" in event:
                event["messages"][-1].pretty_print()
                print()

        snapshot = graph.get_state(config)
        while snapshot.next:
            human_input = input("Human assistance needed. Your response: ")

            last_message = snapshot.values["messages"][-1]
            if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
                tool_call_id = last_message.tool_calls[0]["id"]

                tool_message = ToolMessage(
                    content=human_input,
                    tool_call_id=tool_call_id
                )

                graph.update_state(config, {"messages": [tool_message]})

                for event in graph.stream(None, config, stream_mode="values"):
                    if "messages" in event:
                        event["messages"][-1].pretty_print()
                        print()

                snapshot = graph.get_state(config)
            else:
                break

    except (EOFError, KeyboardInterrupt):
        break
