from models.openai_model import generate
from memory.memory_manager import get_similar_queries

def plan_task(query):
    #  Retrieve similar past queries
    similar = get_similar_queries(query)

    #  Display memory matches (VERY IMPORTANT FOR DEMO)
    print("\n[Memory Matches]")
    if not similar:
        print("No similar past queries found.")
    else:
        for item in similar:
            print("-", item['query'])

    # Build memory context for LLM
    memory_context = ""
    for item in similar:
        memory_context += f"\nPast Query: {item['query']}"

    # Planner prompt (improved)
    prompt = f"""
You are an intelligent planning agent.

User Query:
{query}

Relevant Past Queries:
{memory_context}

Instructions:
1. Explain how the current query relates to past queries (if any)
2. Create a clear step-by-step plan
3. Suggest 3-5 related topics the user can explore next
4. Keep the answer structured

Output format:
RELATION:
PLAN:
RELATED TOPICS:
"""

    # Generate plan using LLM
    response = generate(prompt)

    return response