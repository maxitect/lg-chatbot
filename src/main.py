from graph import stream_graph_updates


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        print("\033[A\033[K", end="")
        stream_graph_updates(user_input)
    except (EOFError, KeyboardInterrupt):
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break
