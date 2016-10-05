from KargerMinCut import kargermincut
import copy
import time

numsimu = 1

file_handle = open("kargerMinCut.txt", "r")
graph = {}

for line in file_handle:
    node = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))
    graph[node] = edges
file_handle.close()

mincut = float ('inf')

time.clock()

for i in range(numsimu):
    graph1={}
    graph1=copy.deepcopy(graph)
    x = kargermincut(graph1)

    if x < mincut:
        mincut = x

print(time.clock())
print(mincut)






