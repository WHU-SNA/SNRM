import networkx as nx
import numpy as np
from scipy.sparse.linalg import svds

dataset = 'Epinions'
seed = 96
edge_path = dataset + '/seed=' + str(seed) + '/train_edges.txt'
G = nx.Graph()
edges = np.loadtxt(edge_path)
for i in range(edges.shape[0]):
    if edges[i][2] > 0:
        G.add_edge(int(edges[i][0]), int(edges[i][1]), weight=1)
    elif edges[i][2] < 0:
        G.add_edge(int(edges[i][0]), int(edges[i][1]), weight=-1)
l = list(G.nodes())
l.sort()
print(l)

num_of_nodes = G.number_of_nodes()
sss = np.zeros((num_of_nodes, num_of_nodes))

for u in range(num_of_nodes):
    print(u)
    for v in range(num_of_nodes):
        common_neighbors = list(nx.common_neighbors(G, u, v))
        if common_neighbors:
            numerator = 0
            for w in common_neighbors:
                if G[u][w]['weight'] == -1:
                    if G[v][w]['weight'] != -1:
                        numerator += G[u][w]['weight'] * G[v][w]['weight']
                else:
                    numerator += G[u][w]['weight'] * G[v][w]['weight']
            sss[u][v] = numerator / len(common_neighbors)

u, s, vt = svds(sss, 32)
sqrtS = np.diag(np.sqrt(s))
emb = u @ sqrtS
np.save('emb,seed=' + str(seed), emb)
print('seed=', seed)
