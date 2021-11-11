import networkx as nx
import random as rand
import matplotlib.pyplot as plt

n=20

G = nx.Graph()
for i in range(n):
    G.add_node(i)

number_edges=rand.randint(2*n,n*n/4)
print(number_edges)

q=0
while(q<number_edges):
    v1=rand.randint(0,n)
    v2=v1
    no_valid_pair=True
    while(no_valid_pair):
        v2=rand.randint(0,n)
        if v2!=v1:
            no_valid_pair=False
    G.add_edge(v1,v2)
    q+=1    

nx.draw(G,with_labels=True)
plt.show()