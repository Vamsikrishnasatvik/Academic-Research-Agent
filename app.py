from orchestrator.orchestrator import run_system
from memory.memory_manager import add_interaction
from memory.view_memory import display_memory

def main():
    while True:
        print("\n1. Ask Query")
        print("2. View Past Chats")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            query = input("\nEnter your research query: ")

            response = run_system(query)

            print("\nFINAL OUTPUT:\n", response)

            # Save memory
            add_interaction(query, response)

        elif choice == "2":
            display_memory()

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()