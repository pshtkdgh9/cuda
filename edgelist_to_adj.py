from itertools import groupby
edges = [(0,4), (0,2), (0,1),(1,0),(1,2), (1,3), (2,4), (2,3), (2,1),(2,0),(3,1),(3,2), (3,5), (3,6),(4,0),(4,2),(4,5),(5,3),(5,4),(5,6),(6,5),(6,3)]

adj = {k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])}
print(adj)

adacency_list = []
for i in adj:
    vertex = adj[i]
    adacency_list.append(np.array(vertex))
print(adacency_list)

## edges : [(0,4), (0,2), (0,1),(1,0),(1,2), (1,3), (2,4), (2,3), (2,1),(2,0),(3,1),(3,2), (3,5), (3,6),(4,0),(4,2),(4,5),(5,3),(5,4),(5,6),(6,5),(6,3)]
## adj : {0: [1, 2, 4], 1: [0, 2, 3], 2: [0, 1, 3, 4], 3: [1, 2, 5, 6], 4: [0, 2, 5], 5: [3, 4, 6], 6: [3, 5]}
## np_adj : [array([1, 2, 4]), array([0, 2, 3]), array([0, 1, 3, 4]), array([1, 2, 5, 6]), array([0, 2, 5]), array([3, 4, 6]), array([3, 5])]
