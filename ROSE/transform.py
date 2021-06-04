import networkx as nx


DATA_DIR = 'input/'
DATASET_NAME = 'Epinions'


for seed in range(6, 106, 10):
    print(seed)
    seed = str(seed)
    G = nx.Graph()
    with open(DATA_DIR + DATASET_NAME + '/seed=' + seed + '/train_edges.txt') as f:
        for line in f:
            line = line.strip().split('\t')
            line = list(map(int, line))
            G.add_edge(line[0], line[1])
    numNodes = max(G.nodes) + 1

    with open(DATA_DIR + DATASET_NAME + '/seed=' + seed + '/aug_train_edges.txt', 'w') as f2w:
        with open(DATA_DIR + DATASET_NAME + '/seed=' + seed + '/train_edges.txt') as f:
            for line in f:
                line = line.strip().split('\t')
                line = list(map(int, line))

                src = line[0]
                des = line[1]
                if line[2] > 0:
                    f2w.write('\t'.join([str(src), str(numNodes * 2 + des)]) + '\n')
                    f2w.write('\t'.join([str(numNodes + src), str(numNodes * 3 + des)]) + '\n')
                elif line[2] < 0:
                    f2w.write('\t'.join([str(src), str(numNodes * 3 + des)]) + '\n')
                    f2w.write('\t'.join([str(numNodes + src), str(numNodes * 2 + des)]) + '\n')

                src = line[1]
                des = line[0]
                if line[2] > 0:
                    f2w.write('\t'.join([str(src), str(numNodes * 2 + des)]) + '\n')
                    f2w.write('\t'.join([str(numNodes + src), str(numNodes * 3 + des)]) + '\n')
                elif line[2] < 0:
                    f2w.write('\t'.join([str(src), str(numNodes * 3 + des)]) + '\n')
                    f2w.write('\t'.join([str(numNodes + src), str(numNodes * 2 + des)]) + '\n')
