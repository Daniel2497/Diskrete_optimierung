import random
import networkx as nx
import matplotlib.pyplot as plt


n = 20
random.seed(42)
pos = {i: (random.gauss(0, 4), random.gauss(0, 4)) for i in range(n)}
print(pos)
G = nx.random_geometric_graph(n,seed=3413, radius=2,pos=pos)
#G=geographical_threshold_graph(n,2,pos=pos)
nx.draw(G,with_labels=True)
plt.show()