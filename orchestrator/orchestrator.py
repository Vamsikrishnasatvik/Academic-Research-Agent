from agents.planner_agent import plan_task 
from agents.retrieval_agent import retrieve_docs, add_document
from agents.summarizer_agent import summarize
from agents.explainer_agent import explain
from agents.recursive_agent import recursive_expand
from tools.pdf_loader import load_pdf


def run_system(query):
    print("[1] Planning...")
    plan = plan_task(query)

    print("[2] Loading PDF...")
    try:
        text = load_pdf("data/sample_paper.pdf")
        if text.strip():
            add_document(text)
        else:
            print("⚠️ PDF loaded but empty text")
    except Exception as e:
        print("⚠️ PDF loading failed:", e)
        text = ""

    print("[3] Retrieving...")
    docs = retrieve_docs(query)

    if not docs:
        print("⚠️ No relevant documents found")

    combined = f"""
USER QUERY:
{query}

RETRIEVED CONTEXT:
{" ".join(docs) if docs else "No relevant context found."}
"""

    print("[4] Recursive Expansion...")
    expanded = recursive_expand(combined, depth=2)

    print("[5] Summarizing...")
    summary = summarize(expanded, query)

    print("[6] Explaining...")
    explanation = explain(summary, query)

    return f"""
================ FINAL OUTPUT ================

PLAN:
{plan}

--------------------------------------------

SUMMARY:
{summary}

--------------------------------------------

EXPLANATION:
{explanation}

============================================
"""