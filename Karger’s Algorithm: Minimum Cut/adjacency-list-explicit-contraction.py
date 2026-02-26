import random
import copy
import math


# Read graph from file
def load_graph(filename):
    graph = {}
    with open(filename, "r") as f:
        for line in f:
            nums = list(map(int, line.strip().split()))
            graph[nums[0]] = nums[1:]
    return graph

# Contract a random edge
def contract(graph):
    # Pick random vertex u
    u = random.choice(list(graph.keys()))
    # Pick random neighbor v
    v = random.choice(graph[u])

    # Merge v into u
    graph[u].extend(graph[v])

    # Redirect edges from v to u
    for neighbor in graph[v]:
        graph[neighbor] = [u if x == v else x for x in graph[neighbor]]

    # Remove self-loops
    graph[u] = [x for x in graph[u] if x != u]

    # Delete vertex v
    del graph[v]


# Run one trial of Karger's algorithm
def karger_min_cut(original_graph):
    graph = copy.deepcopy(original_graph)

    while len(graph) > 2:
        contract(graph)

    # When two vertices remain, the cut size
    # is the number of edges between them
    remaining_vertex = list(graph.keys())[0]
    return len(graph[remaining_vertex])


# Run many trials
def find_min_cut(graph, trials):
    min_cut = float("inf")

    for _ in range(trials):
        cut = karger_min_cut(graph)
        if cut < min_cut:
            min_cut = cut

    return min_cut


# Main 
if __name__ == "__main__":
    graph = load_graph("TestAdjacencyList.txt")

    n = len(graph)

    # Theoretical recommendation: O(n^2 log n)
    trials = int(n**2 * math.log(n))

    print("Running", trials, "trials...")

    min_cut = find_min_cut(graph, trials)

    print("Minimum cut found:", min_cut)
