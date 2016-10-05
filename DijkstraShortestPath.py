def dijkstrashortestpath(source,graph):

    V = graph.keys() | set()
    current = source
    dist={}

    prev=[]

    for v in V:
        dist[v] = 1000000
    dist[source]=0


    while len(V) >=1:
        distupdate = {k: dist[k] for k in V}
        current = min(distupdate, key=distupdate.get)
        V.discard(current)
        prev.append(current)

        for w in graph[current]:
            if w in V:
                alt = dist[current] + graph[current][w]
            #print (w, alt)
                if alt < dist[w]:
                    dist [w] = alt
    return dist





