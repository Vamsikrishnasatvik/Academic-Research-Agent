from memory.memory_manager import load_memory

def display_memory():
    memory = load_memory()

    if not memory:
        print("No past chats found.")
        return

    print("\n===== CHAT HISTORY =====\n")
    for i, item in enumerate(memory):
        print(f"{i+1}. Q: {item['query']}")
        print(f"A Summary: {item['response'][:150]}...")