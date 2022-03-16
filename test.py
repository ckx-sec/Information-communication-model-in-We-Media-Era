import itertools
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from typing import List

typeList: List[str] = ["sport", "fashion", "food", "tourism", "furniture", "history", "vehicle", "anime", "game",
                  "gossip", "geography", "language", "movie", "music", "photography", "finance", "technology", "news"]

f = open("nodes", "r", encoding="utf-8").readlines()
edge = []
node = []
for i in f:
    i = i.split(',')
    node.append(i[-1].strip())
f1 = open("edges", "r", encoding="utf-8").readlines()
for i in f1:
    i = i.split(',')
    a = (int(i[0]), int(i[1].strip()))
    edge.append(a)


G = nx.Graph()
node_and_dict = []
for i in node:
    node_and_dict.append(
        (int(i), dict(map(lambda x: (x, random.random()), typeList))))
    #G.add_node(i, interest=interest)
G.add_nodes_from(node_and_dict)
G.add_edges_from(edge)
print(G.number_of_nodes())
print(G.number_of_edges())
# print(G.degree)
print(max(G.degree, key=lambda x: x[1]))
print(G.nodes[11])
# print(nx.adjacency_matrix(G).todense())
crap = nx.adjacency_matrix(G).todense(out=np.ndarray)

#     for c in row:
#         print(c, end=',')
# f2.write("{}".format(np.array(nx.adjacency_matrix(G).todense())))
# nx.draw(G)
# plt.savefig("path.png")
