from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge
from UnionFind import UnionFind
import heapq

def KruskalMST(graph:EdgeWeightedGraph):

    MST = []
    EdgeSequence=[]
    UF = UnionFind(graph.numVertices())

    #Pre-processing the edges
    PQ = []
    for item in graph.adj:
        PQ += graph.adj[item]
    heapq.heapify(PQ)

    while (len(PQ)>0) & (len(MST) < graph.numVertices()-1):
        e = heapq.heappop(PQ)
        v = e.either()
        w = e.other(v)

        if (UF.connected(v,w)):
            continue
        else:
            UF.union(v,w)
            heapq.heappush(MST, e)
            EdgeSequence.append(e)

        cluster = set()
        for item in UF.id:
            cluster.add(item)

        print ("cluster:", cluster, len(cluster))
        print (e.weight)
    return MST
    #print(PQ)


