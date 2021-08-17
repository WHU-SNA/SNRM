import networkx as nx
import numpy as np
import random as rd


# ========== For convenience, we make the node index in G start from 0. ==========
G = nx.Graph()
G.add_edge(0, 1, weight=1)
G.add_edge(0, 2, weight=-1)
G.add_edge(1, 2, weight=1)
G.add_edge(2, 3, weight=1)
G.add_edge(3, 4, weight=1)
G.add_edge(3, 5, weight=-1)

A = nx.adjacency_matrix(G).todense()
A = np.abs(A)
invD = np.diag(1 / np.array(A.sum(axis=0))[0])
P = np.array(invD @ A)

walks_num = 1e+6

# ========== Starting from node 1 of our paper (i.e., node 0 in G) ==========
positive_paths = []
negative_paths = []
for i in range(int(walks_num)):
    pre_node = 0
    node = 0
    length = 0
    sign = 1
    while node != 3:
        # Node 3 in G corresponds to the node 4 of our paper.
        length += 1
        node = rd.choices(range(G.number_of_nodes()), weights=P[pre_node, :])[0]
        sign *= G[pre_node][node]['weight']
        pre_node = node
    if sign > 0:
        positive_paths.append(length)
    else:
        negative_paths.append(length)
if len(positive_paths) == 0:
    print('positive SAFT of 1 to 4: Inf')
else:
    print('positive SAFT of 1 to 4:', round(sum(positive_paths) / len(positive_paths), 2))
if len(negative_paths) == 0:
    print('negative SAFT of 1 to 4: Inf')
else:
    print('negative SAFT of 1 to 4:', round(sum(negative_paths) / len(negative_paths), 2))


# ========== Starting from node 2 of our paper (i.e., node 1 in G) ==========
positive_paths = []
negative_paths = []
for i in range(int(walks_num)):
    pre_node = 1
    node = 1
    length = 0
    sign = 1
    while node != 3:
        length += 1
        node = rd.choices(range(G.number_of_nodes()), weights=P[pre_node, :])[0]
        sign *= G[pre_node][node]['weight']
        pre_node = node
    if sign > 0:
        positive_paths.append(length)
    else:
        negative_paths.append(length)
if len(positive_paths) == 0:
    print('positive SAFT of 2 to 4: Inf')
else:
    print('positive SAFT of 2 to 4:', round(sum(positive_paths) / len(positive_paths), 2))
if len(negative_paths) == 0:
    print('negative SAFT of 2 to 4: Inf')
else:
    print('negative SAFT of 2 to 4:', round(sum(negative_paths) / len(negative_paths), 2))


# ========== Starting from node 3 of our paper (i.e., node 2 in G) ==========
positive_paths = []
negative_paths = []
for i in range(int(walks_num)):
    pre_node = 2
    node = 2
    length = 0
    sign = 1
    while node != 3:
        length += 1
        node = rd.choices(range(G.number_of_nodes()), weights=P[pre_node, :])[0]
        sign *= G[pre_node][node]['weight']
        pre_node = node
    if sign > 0:
        positive_paths.append(length)
    else:
        negative_paths.append(length)
if len(positive_paths) == 0:
    print('positive SAFT of 3 to 4: Inf')
else:
    print('positive SAFT of 3 to 4:', round(sum(positive_paths) / len(positive_paths), 2))
if len(negative_paths) == 0:
    print('negative SAFT of 3 to 4: Inf')
else:
    print('negative SAFT of 3 to 4:', round(sum(negative_paths) / len(negative_paths), 2))


# ========== Starting from node 5 of our paper (i.e., node 4 in G) ==========
positive_paths = []
negative_paths = []
for i in range(int(walks_num)):
    pre_node = 4
    node = 4
    length = 0
    sign = 1
    while node != 3:
        length += 1
        node = rd.choices(range(G.number_of_nodes()), weights=P[pre_node, :])[0]
        sign *= G[pre_node][node]['weight']
        pre_node = node
    if sign > 0:
        positive_paths.append(length)
    else:
        negative_paths.append(length)
if len(positive_paths) == 0:
    print('positive SAFT of 5 to 4: Inf')
else:
    print('positive SAFT of 5 to 4:', round(sum(positive_paths) / len(positive_paths), 2))
if len(negative_paths) == 0:
    print('negative SAFT of 5 to 4: Inf')
else:
    print('negative SAFT of 5 to 4:', round(sum(negative_paths) / len(negative_paths), 2))


# ========== Starting from node 6 of our paper (i.e., node 5 in G) ==========
positive_paths = []
negative_paths = []
for i in range(int(walks_num)):
    pre_node = 5
    node = 5
    length = 0
    sign = 1
    while node != 3:
        length += 1
        node = rd.choices(range(G.number_of_nodes()), weights=P[pre_node, :])[0]
        sign *= G[pre_node][node]['weight']
        pre_node = node
    if sign > 0:
        positive_paths.append(length)
    else:
        negative_paths.append(length)
if len(positive_paths) == 0:
    print('positive SAFT of 6 to 4: Inf')
else:
    print('positive SAFT of 6 to 4:', round(sum(positive_paths) / len(positive_paths), 2))
if len(negative_paths) == 0:
    print('negative SAFT of 6 to 4: Inf')
else:
    print('negative SAFT of 6 to 4:', round(sum(negative_paths) / len(negative_paths), 2))
