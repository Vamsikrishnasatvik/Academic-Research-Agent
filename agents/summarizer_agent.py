from models.local_model import generate

def summarize(text, query):
    prompt = f"""
You are a research assistant.

Answer ONLY based on the given context.

Query:
{query}

Context:
{text[:3000]}
"""
    return generate(prompt)