import random

# Converts file into: list of vertices & list of edges (edge list)
def load_edges(filename):
    # To store edges as (u, v)
    edges = []
    # Using a set to automatically avoid duplicates
    vertices = set()

    with open(filename, "r") as f:
        for line in f:
            nums = list(map(int, line.strip().split()))

            # First number is the vertex
            u = nums[0]
            # Add it to vertex set
            vertices.add(u)

            # All other numbers are neighbours
            for v in nums[1:]:

                vertices.add(v)
                # To avoid (u, v) duplicates, we only add edge if u < v
                if u < v:
                    edges.append((u, v))

    return list(vertices), edges


# Runs one trial of Karger's algorithm. Uses Union-Find.
def karger_min_cut(vertices, edges):
    # parent[v] is the "representative" (leader)
    # of the component that vertex v belongs to
    parent = {v: v for v in vertices}

    # Returns the representative of vertex v
    def find(v):
        while parent[v] != v:
            # Path compression: Make v point directly to its grandparent
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    # Merges the components of u and v
    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        # Make root_u point to root_v
        parent[root_u] = root_v

    # Repeatedly contract edges until 2 left
    remaining = len(vertices)
    while remaining > 2:

        # Randomly select an edge
        u, v = random.choice(edges)

        # Find which components u and v belong to
        root_u = find(u)
        root_v = find(v)

        # If they belong to different components:
        if root_u != root_v:

            union(root_u, root_v)  # Merge components
            remaining -= 1         # One fewer component


    # Cut size = no. of edges connecting last 2 components
    cut = 0

    for u, v in edges:
        if find(u) != find(v):
            cut += 1

    return cut

# Runs Karger's algorithm multiple times
# Keeps the smallest cut found
def find_min_cut(vertices, edges, trials):

    min_cut = float("inf")

    for i in range(trials):

        cut = karger_min_cut(vertices, edges)

        # Keep the smallest cut seen so far
        if cut < min_cut:
            min_cut = cut

        # Optional: progress printing
        if i % 1000 == 0:
            print("Trial", i, "Current best:", min_cut)

    return min_cut

# Main
if __name__ == "__main__":
    # Load graph
    vertices, edges = load_edges("kargerMinCut.txt")

    n = len(vertices)

    # Theoretical recommendation: O(n^2 log n)
    # But in practice, n^2 trials is usually enough.
    trials = n * n

    print("Running", trials, "trials...")

    result = find_min_cut(vertices, edges, trials)

    print("Minimum cut found:", result)
