from Edge import Edge


class EdgeWeightedGraph:

    def __init__(self,V):
        self.V = V
        self.E = 0
        self.adj = {}

        for v in range(1, V+1):
            self.adj[v]=[]

    def addEdge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.adj[v].append(edge)
        self.adj[w].append(edge)

    def numVertices(self):
        return self.V


