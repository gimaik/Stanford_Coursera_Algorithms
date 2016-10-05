import operator
import heapq
from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge


def main():
    V = set()
    file_handle = open("Edges.txt", 'r')

    for line in file_handle:

        if len(line.split()) <= 2:
            numNodes = int(line.split()[0])
            numEdges = int(line.split()[1])
            graph = EdgeWeightedGraph(numNodes)
        else:
            v = int(line.split()[0])
            w = int(line.split()[1])
            weight = int(line.split()[2])
            edge = Edge(v, w, weight)
            graph.addEdge(edge)

            V.add(v)
            V.add(w)

    # for item in graph.adj[1]:
    #     print(item.either(),item.other(item.either()), item.weight)
    #
    # print ("min",minEdge(graph.adj[1]).weight)
    # #print(graph.adj[1][1].either(),graph.adj[1][1].other(graph.adj[1][1].either()), graph.adj[1][1].weight)
    # #print(graph.adj[1][2].either(),graph.adj[1][2].other(graph.adj[1][2].either()), graph.adj[1][2].weight)
    # #print(graph.adj[1][1] > graph.adj[1][2] )

    Primedges = primMST(graph, V, 1)
    sum = 0
    for item in Primedges:
        sum += item.weight

    print (sum)

def primMST(graph, V, source):
    explored = set()
    explored.add(source)
    T = []

    X = graph.adj[source]
    heapq.heapify(X)

    while len(X) > 0:
        e = heapq.heappop(X)

        u = e.either()
        v = e.other(u)

        if u not in explored:
            explored.add(u)
            T.append(e)
            X = X + graph.adj[u]

        elif v not in explored:
            explored.add(v)
            T.append(e)
            X = X + graph.adj[v]

        heapq.heapify(X)


        # print("X", X)

    return T


def minEdge(listOfEdges):
    return min(listOfEdges)


main()
