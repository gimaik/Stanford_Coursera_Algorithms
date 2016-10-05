from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge
from Kruskal import KruskalMST

def LoadGraph(filename):

    file_handle = open(filename, 'r')
    for line in file_handle:

        if len(line.split()) <= 1:
            numNodes = int(line.split()[0])
            graph = EdgeWeightedGraph(numNodes)
        else:
            v = int(line.split()[0])
            w = int(line.split()[1])
            weight = int(line.split()[2])
            edge = Edge(v, w, weight)
            graph.addEdge(edge)

    return graph






def main():
    filename = "clustering1.txt"
    graph = LoadGraph(filename)

    print(graph)
    test = KruskalMST(graph)
    print(test)


main()
