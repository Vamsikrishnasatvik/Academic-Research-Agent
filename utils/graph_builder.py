import networkx as nx

def build_graph(text, citations):
    G = nx.Graph()
    G.add_node("root")

    for c in citations:
        G.add_edge("root", c)

    return G