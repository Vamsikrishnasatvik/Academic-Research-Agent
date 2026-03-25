from agents.citation_agent import get_citations
from agents.retrieval_agent import retrieve_docs
visited = set()

def recursive_expand(text, depth=2, visited=None):
    if visited is None:
        visited = set()

    if depth == 0:
        return text

    citations = get_citations(text)
    expanded = text

    for c in citations:
        if c in visited:
            continue
        visited.add(c)

        results = retrieve_docs(c)
        for r in results:
            expanded += "\n" + recursive_expand(r, depth - 1, visited)

    return expanded