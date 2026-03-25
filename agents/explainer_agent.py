from models.local_model import generate

def explain(text, query):
    prompt = f"""
Explain this clearly for a beginner.

Topic: {query}

Content:
{text}
"""
    return generate(prompt)