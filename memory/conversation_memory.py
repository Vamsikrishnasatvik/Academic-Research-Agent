import json
import os

MEMORY_FILE = "memory/chat_history.json"

def save_memory(role, content):
    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    data.append({"role": role, "content": content})

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)