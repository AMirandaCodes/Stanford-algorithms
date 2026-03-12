# Dijkstra’s Shortest-Path Algorithm

The goal of this assignment is to compute **shortest-path distances** in a weighted graph using **Dijkstra’s algorithm**.
The algorithm finds the minimum distance from a **source vertex** to every other vertex in a graph with **non-negative edge weights**.


## Problem Description

You are given a file (`dijkstraData.txt`) containing an **adjacency list representation of an undirected weighted graph**.

- The graph contains **200 vertices** labeled from `1` to `200`.
- Each row corresponds to one vertex.
- The first number is the **vertex label**.
- The remaining entries represent **adjacent vertices and edge lengths**.

**Example entry:** 6  141,8200

This means:
- There is an edge between vertex **6** and vertex **141**.
- The edge has length **8200**.

## Objective

Run **Dijkstra’s algorithm** using **vertex 1 as the source** and compute the shortest-path distances from vertex `1` to every other vertex.

If a vertex is unreachable from the source, its distance is defined as:
1000000

The assignment requires reporting the shortest-path distances to the following vertices:
7, 37, 59, 82, 99, 115, 133, 165, 188, 197


---

## Algorithm Overview

Dijkstra’s algorithm works by repeatedly selecting the **closest unexplored vertex** and updating the shortest known distances to its neighbors.

### Basic Idea

1. Start from the **source vertex** with distance `0`.
2. Maintain a set of **processed vertices** whose shortest distance is known.
3. Repeatedly:
   - Select the unexplored vertex with the **smallest tentative distance**
   - Add it to the processed set
   - Relax its outgoing edges
4. Continue until all vertices are processed.

### Time Complexity

Two common implementations exist:

- **Simple implementation:** `O(mn)`

- **Heap-based implementation:** `O((m + n) log n)`

where:

- `n` = number of vertices  
- `m` = number of edges

---

## Approach Overview
Out of curiosity and experimentation, I implemented two versions of Dijkstra’s algorithm.

## Version 1 — Straightforward Implementation (Frontier Scan)

This implementation follows the naive approach described in the lectures.

### Characteristics

- Maintains:
  - `X` → Set of processed vertices
  - `A` → Dictionary of shortest distances
- At each step:
  - Scans **all frontier edges** between explored and unexplored vertices
  - Selects the edge with the **minimum greedy score**

The greedy score is: `A[v] + length(v, w)`, where `v` is an explored vertex and `w` is an unexplored neighbor.

### Pros

- Very easy to understand
- Closely matches the conceptual explanation of Dijkstra’s algorithm
- Good for learning purposes

### Cons

- Inefficient for large graphs
- Repeatedly scans many edges
- Time complexity grows quickly with graph size

## Version 2 — Heap-Based Implementation (Priority Queue)

The second implementation uses a **min-heap (priority queue)** to efficiently select the next vertex with the smallest tentative distance.

### Key Idea

Instead of scanning all frontier edges each iteration, a **heap** always provides the vertex with the smallest distance.

This reduces the amount of work needed to select the next vertex.

### Characteristics

- Uses Python’s `heapq` module
- Maintains:
  - `dist` → Dictionary of shortest known distances
  - `heap` → Priority queue of `(distance, vertex)`
- Supports **efficient distance updates**

Outdated heap entries are skipped when popped from the heap.

## Key Differences Between the Two Implementations

| Aspect | Version 1 (Frontier Scan) | Version 2 (Heap-Based) |
|------|------|------|
| Vertex selection | Scans all frontier edges | Uses a priority queue |
| Data structures | Sets and dictionaries | Min-heap + dictionary |
| Complexity | **O(mn)** | **O((m+n) log n)** |
| Efficiency | Slower for large graphs | Much faster |
| Scalability | Limited | Scales well |

---

## Why the Heap-Based Version Is Better

The heap-based version avoids repeatedly scanning the entire frontier.

Instead:

- The heap always returns the **next closest vertex**
- Distance updates are **logarithmic time**

Benefits include:

- Much better performance on large graphs
- Cleaner separation between:
  - distance tracking
  - vertex selection
- More representative of **real-world implementations of Dijkstra’s algorithm**

Although the simple implementation works fine for small graphs (like the 200-vertex graph in this assignment), the heap-based approach becomes essential for **large-scale graphs**.

---

## Notes

- The graph edges have **non-negative weights**, which is required for Dijkstra’s algorithm to work correctly.
- The assignment defines unreachable distances as `1000000` instead of infinity.
- Python’s `heapq` does not support key decrease operations directly, so the implementation pushes updated distances and skips outdated entries when they are popped.

## What This Assignment Demonstrates

This assignment highlights:

- The importance of **efficient data structures** in graph algorithms
- How different implementations of the same algorithm can lead to large performance differences
- The use of **priority queues** in shortest-path problems
- The practical trade-offs between conceptual simplicity and computational efficiency
