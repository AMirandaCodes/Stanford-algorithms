import math

# Load graph (adjacency list)
def load_graph(filename):
    graph = {}
    with open(filename,"r") as f:
        for line in f:
            parts = line.split()
            v = int(parts[0])
            graph[v] = []

            for edge in parts[1:]:
                w, length = edge.split(",")
                graph[v].append((int(w), int(length)))

    return graph

# Dijkstra algorithm
def dijkstra(graph, origin=1):
    
    A = {} # Shortest distances
    A[origin] = 0
    X = {1} # Processed vertices

    while X != set(graph.keys()):

        best_score = 1000000 # As instructed, instead of ∞
        best_vertex = None

        # Scan frontier edges
        for v in X:
            for w, length in graph[v]:

                if w not in X:
                    # Greedy score
                    score = A[v] + length

                    # Pick smallest score
                    if score < best_score:
                        best_score = score
                        best_vertex = w

        # Add vertex to X
        X.add(best_vertex)
        # Record shortest distance
        A[best_vertex] = best_score

    return A

if __name__ == "__main__":
    graph = load_graph('dijkstraData.txt')
    distances = dijkstra(graph)

    # Specific vertices to get their distances from
    targets = (7, 37, 59, 82, 99, 115, 133, 165, 188, 197)
    
    for v in targets:
        print("Vertex "+ str(v) + ": " + str(distances[v]))
