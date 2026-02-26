# Returns: Adjacency (& reversed) list, & number of vertices
def load_graph(filename):
    graph = {}
    graph_rev = {}
    max_node = 0

    with open(filename, "r") as f:
        for line in f:
            u, v = map(int, line.split())
            max_node = max(max_node, u, v)
        
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            if u not in graph_rev:
                graph_rev[u] = []
            if v not in graph_rev:
                graph_rev[v] = []

            graph[u].append(v)
            graph_rev[v].append(u)

        for i in range(1, max_node + 1):
            if i not in graph:
                graph[i] = []
            if i not in graph_rev:
                graph_rev[i] = []

    return graph, graph_rev, max_node

def DFS_Loop(graph, graph_rev):
    global t,s
    t = 0

    # First pass
    for i in sorted(graph.keys(), reverse=True):
        if not explored[i]:
            DFS(graph_rev, i, True)
    
    # Reset Explored before second pass
    for i in graph.keys():
        explored[i] = False

    # Second pass: Processes nodes in decreasing finishing time order
    for i in range(n, 0, -1):
        vertex = order[i]
        if not explored[vertex]:
            s = vertex
            DFS(graph, vertex, False)

# If first pass: assigns finishing time
# If second pass: assigns leader
def DFS(graph, i, first_pass):
    global t, s
    explored[i] = True

    if not first_pass:
        # Every node reached in that DFS shares the same leader => same SCC
        leader[i] = s

    for j in graph[i]:
        if not explored[j]:
            DFS(graph, j, first_pass)

    # Assigns finishing times
    if first_pass:
        t += 1
        order[t] = i
    
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1000000)
    
    graph, graph_rev, n = load_graph('TestSCC.txt')

    # Global structures
    explored = [False] * (n+1)
    finishing_time = [0] * (n+1)
    leader = [0] * (n+1)
    order = [0] * (n+1)
    t = 0

    DFS_Loop(graph, graph_rev)

    # Counts nodes per leader
    from collections import Counter
    sizes = Counter(leader[1:])

    # Outputs largest SCC sizes
    largest = sorted(sizes.values(), reverse=True)[:5]
    print(largest)