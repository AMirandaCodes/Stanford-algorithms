import heapq

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

def dijkstra_heap(graph, origin=1):

    dist = {v: 1000000 for v in graph}
    dist[origin] = 0

    heap = [(0, origin)] # (distance, vertex)

    while heap:

        current_dist, v = heapq.heappop(heap)

        # Skip outdated entries
        if current_dist > dist[v]:
            continue

        for w, length in graph[v]:

            new_dist = dist[v] + length

            if new_dist < dist[w]:
                dist[w] = new_dist
                heapq.heappush(heap, (new_dist, w))
    
    return dist

if __name__ == "__main__":
    graph = load_graph('dijkstraData.txt')
    distances = dijkstra_heap(graph)

    # Specific vertices to get their distances from
    targets = (7, 37, 59, 82, 99, 115, 133, 165, 188, 197)
    
    for v in targets:
        print("Vertex "+ str(v) + ": " + str(distances[v]))