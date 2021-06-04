import networkx as nx
import numpy as np
from scipy.sparse.linalg import svds


dataset = 'Alpha'
dim = 32
print(dataset)
for seed in range(6, 106, 10):
    print(seed)
    G = nx.Graph()
    with open('input/' + dataset + '/seed=' + str(seed) + '/train_edges.txt') as f:
        for edge in f:
            edge = edge.strip().split('\t')
            G.add_edge(edge[0], edge[1])
    A = np.asarray(nx.adjacency_matrix(G).todense())
    D = A @ np.ones((G.number_of_nodes(), 1))
    D = np.diag(D.flatten())
    L = D - A
    L_pinv = np.linalg.pinv(L)

    GV = D.sum().sum()
    tmp = L_pinv @ D @ np.ones((G.number_of_nodes(), 1))
    AFT = -L_pinv * GV + tmp - tmp.T + np.diag(L_pinv) * GV
    u, s, vt = svds(AFT, dim)
    sqrtS = np.diag(np.sqrt(s))
    out_emb = u @ sqrtS
    out_emb = out_emb[:, ::-1]
    in_emb = (sqrtS @ vt).T
    in_emb = in_emb[:, ::-1]

    np.save(dataset + '/seed=' + str(seed) + '/AFT/out_emb', out_emb)
    np.save(dataset + '/seed=' + str(seed) + '/AFT/in_emb', in_emb)
