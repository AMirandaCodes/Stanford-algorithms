# Karger’s Algorithm — Minimum Cut

The goal of this assignment is to compute the **minimum cut** of an undirected graph using **Karger’s randomized contraction algorithm**.

Unlike deterministic graph algorithms, Karger’s algorithm is probabilistic: it must be executed multiple times to obtain the correct answer with high probability.

## Problem Description

You are given a text file representing an **undirected graph** in adjacency list format.

Each row corresponds to a vertex:
- The first number is the vertex label.
- The remaining numbers are the vertices adjacent to it.

### Objective

Compute the **minimum cut** of the graph.

A **cut** is a partition of the vertices into two non-empty sets. The size of the cut is the number of edges crossing between those two sets.

The **minimum cut** is the smallest such value over all possible partitions.

Because Karger’s algorithm is randomized, it must be run many times, and the smallest cut found across all trials is returned.

## Algorithm Overview

Karger’s algorithm works as follows:

1. While more than two vertices remain:
   - Pick a random edge `(u, v)`
   - Contract (merge) the two vertices
   - Remove self-loops
2. When only two supernodes remain:
   - The number of crossing edges between them is a cut
3. Repeat many times and keep the smallest cut found

### Time Complexity

- One trial: **O(n²)** (depending on implementation)
- To achieve high probability of success: **O(n² log n)** trials

---

## Approach Overview

Out of curiosity and experimentation, I implemented **two different versions** of Karger’s algorithm:

### Version 1 — Adjacency List with Explicit Contraction

- Uses a dictionary-based adjacency list
- Explicitly merges vertices during contraction
- Removes self-loops manually
- Deep copies the graph for each trial

#### Characteristics
- Conceptually straightforward
- Closely follows the lecture description
- Works well for small graphs
- Becomes slow for larger graphs due to:
  - Frequent deep copies
  - Rebuilding adjacency lists
  - Repeated list traversals

### Version 2 — Edge List + Union-Find (Disjoint Set)

- Converts the graph into:
  - A list of vertices
  - A list of edges
- Uses a **Union-Find (Disjoint Set)** data structure
- Avoids explicitly modifying adjacency lists
- Contracts components logically instead of physically

#### Characteristics
- More memory efficient
- Avoids deep copying large graph structures
- Faster in practice
- Cleaner separation between:
  - Contraction logic
  - Edge counting
- Scales significantly better for large numbers of trials

## Key Differences Between the Two Implementations

| Aspect | Version 1 (Adjacency List) | Version 2 (Union-Find) |
|---------|----------------------------|------------------------|
| Graph representation | Dictionary of adjacency lists | Edge list + vertex set |
| Contraction | Physically merges vertices | Logical merging via Union-Find |
| Memory usage | High (deep copies per trial) | Lower |
| Self-loop handling | Manual removal | Automatically ignored |
| Performance | Slower for many trials | Faster and cleaner |
| Scalability | Limited | Much better |

### Why Version 2 Is Better

- Avoids repeated structural graph modifications
- Uses efficient **path compression** in Union-Find
- Separates graph structure from contraction logic
- More suitable for running thousands of trials
- Closer to how large-scale randomized graph algorithms are implemented in practice

Version 1 is great for learning.  
Version 2 is better for performance and scalability.

## Running Multiple Trials

Since Karger’s algorithm succeeds with probability: `≥ 2 / (n(n − 1))` it must be repeated many times.

In my implementation:

- **Theoretical recommendation:** `O(n² log n)` trials
- **Practical compromise:** `n²` trials often sufficient

The algorithm keeps track of the **smallest cut found** across all trials.

## Notes

- The algorithm is randomized — results may vary between runs.
- Increasing the number of trials increases confidence in correctness.
- This assignment highlights:
  - The power of randomization in algorithms
  - The difference between theoretical guarantees and practical performance
  - The importance of choosing the right data structures
