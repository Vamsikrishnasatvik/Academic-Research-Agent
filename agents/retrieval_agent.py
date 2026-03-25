from tools.vector_store import SimpleVectorStore

store = SimpleVectorStore()

def retrieve_docs(query):
    return store.search(query)

def add_document(document_text):
    chunks = document_text.split("\n\n")
    for chunk in chunks:
        if len(chunk.strip()) > 50:
            store.add(chunk)