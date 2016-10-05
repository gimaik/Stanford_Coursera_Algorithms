import random
import numpy as np

def kargermincut(graph):

    added = []
    while len(graph) > 2:
        start = np.random.choice(list(graph.keys()), replace=False)
        finish = np.random.choice(list(graph[start]), replace=False)

        added.append(finish)
        for edge in graph[finish]:
            graph[edge].remove(finish)
            if edge != start:
                graph[start].append(edge)
                graph[edge].append(start)
        del graph[finish]

    finalkey = list(graph.keys())[0]
    return len(graph[finalkey])

