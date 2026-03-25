def extract_citations(text):
    # Dummy citations (for demo)
    if "attention" in text.lower():
        return ["Attention Mechanism Paper (2014)"]
    if "rnn" in text.lower():
        return ["RNN Paper (1997)"]
    return []