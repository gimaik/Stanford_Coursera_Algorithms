# set Global variable
Stack = []
TrackerStack = []
explored = set()
current = None
leader = {}
finishtime = {}
output = []
t = 0
added=set()

def load_graph(filename, n, reverse):
    file_handle = open(filename, "r")
    graph = {}

    for keys in range(1, n + 1):
        graph[keys] = []

    for line in file_handle:
        v = int(line.split()[0])
        w = int(line.split()[1])

        if not reverse:
            graph[v].append(w)
        else:
            graph[w].append(v)
    file_handle.close()

    return graph

# / Depth First Seach Stack Method
def dfs_stack(graph, source, leadertrue, finishtimetrue):
    global explored, leader, Stack, TrackerStack, finishtime, t

    Stack.append(source)
    explored.add(source)
    leader[current]=[]

    while len(Stack) > 0:
        vertex = Stack.pop()
        TrackerStack.append(vertex)

        if leadertrue:
            leader[current].append(vertex)

        stacklengthbefore = len(Stack)
        for vertices in graph[vertex]:
            if vertices not in explored:
                explored.add(vertices)
                Stack.append(vertices)

        if finishtimetrue:
            if (len(Stack)==stacklengthbefore):
                t+=1
                finishtime[t]=TrackerStack.pop()

    if finishtimetrue:
        while len(TrackerStack)>0:
            t+=1
            finishtime[t] = TrackerStack.pop()



def dfs_loop(graph, leadertrue, finishtimetrue):

    global current, finishtime
    n = max(graph.keys())

    for k in range(n, 0, -1):

        if finishtimetrue:
            vertex = k
        else:
            vertex = finishtime[k]

        if vertex not in explored:
            current = vertex
            dfs_stack(graph, current, leadertrue, finishtimetrue)



def kosarajuSCC(graph, graphrev):
    global explored, current, leader, output
    dfs_loop(graphrev, False, True)
    explored.clear()
    dfs_loop(graph, True, False)

def extractresults():
    global output

    for item in leader:
        output.append(len(leader[item]))

    output.sort(reverse=True)

    outputlength = len(output)
    if outputlength <=5:
        print("Output: ", output)
    else:
        print("Output: ", output[0:5])

m =875714
graph = load_graph("SCC.txt", m, False)
graphrev = load_graph("SCC.txt", m, True)
kosarajuSCC(graph, graphrev)
extractresults()
