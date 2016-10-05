from DijkstraShortestPath import dijkstrashortestpath
from Edge import Edge

file_handle = open ("dijkstraData.txt", "r")
graph = {}
dist ={}

for line in file_handle:
    v = int(line.split()[0])
    graph[v] = {}

    for vertex in line.split()[1:]:
        edge = Edge(v, int(vertex.split(",")[0]), int(vertex.split(",")[1]))
        graph[v][edge.other(v)] = edge.weight
file_handle.close()


dist = dijkstrashortestpath(1,graph)

for keys in (7,37,59,82,99,115,133,165,188,197):
    print(dist[keys])


#print(dist)












