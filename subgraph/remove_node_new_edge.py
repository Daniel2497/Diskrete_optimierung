import networkx as nx
G = nx.path_graph(3)
print(list(G.edges))
G.remove_node(1)
G.add_edge(0,2)
print(list(G.edges))