# Kosaraju’s Algorithm — Strongly Connected Components (SCC)

The goal of this assignment is to compute the **Strongly Connected Components (SCCs)** of a very large directed graph using **Kosaraju’s two-pass algorithm**.

This is one of the most challenging programming assignments of the course due to the **size of the graph** and the need for careful memory management.

## Problem Description

You are given a file (`SCC.txt`) containing the edges of a **directed graph**.

- Vertices are labeled from **1 to 875,714**
- Each row represents one directed edge
- The first column is the **tail**
- The second column is the **head**

Example: `2 47646`

This means there is a directed edge from vertex `2` to vertex `47646`.

## Objective

Implement Kosaraju’s algorithm to compute the **sizes of the 5 largest SCCs**.

The final output must list the five largest SCC sizes in decreasing order. If fewer than five SCCs exist, the remaining values should be `0`.

## Algorithm Overview

Kosaraju’s algorithm works in **two passes of DFS**:

### First Pass (on the reversed graph)
- Run DFS on the reversed graph
- Compute **finishing times** for each vertex

### Second Pass (on the original graph)
- Process vertices in **decreasing order of finishing times**
- Each DFS in this phase identifies one SCC
- Track the size of each SCC

### Time Complexity
- **O(m + n)**, where:
  - `n` = number of vertices
  - `m` = number of edges

The algorithm is linear in theory — but implementation details heavily affect practical performance.

---

## Approach Overview

Due to the scale of the graph (875,714 vertices), I implemented **two different versions** of Kosaraju’s algorithm.

## Version 1 — Recursive DFS

This implementation follows the algorithm exactly as described in the lectures.

### Characteristics

- Uses recursive DFS
- Uses global variables to track:
  - `explored`
  - `leader`
  - `finishing times`
- Builds:
  - Adjacency list
  - Reversed adjacency list
- Increases recursion limit manually

### Pros

- Very clean and conceptually aligned with the lecture explanation
- Easy to reason about
- Good for small and medium graphs

### Cons

- Heavy recursion depth
- Risk of stack overflow
- Slower for very large graphs
- Memory-intensive due to recursion stack

This version works well for test files but struggles with the full dataset.

## Version 2 — Iterative DFS (Stack-Based)

To handle the large graph efficiently, I rewrote DFS using an **explicit stack**, eliminating recursion entirely.

### Key Idea

Instead of: `DFS(node): for each neighbor: DFS(neighbor)`, I simulate recursion manually using a stack that stores:
- Current node
- Index of next neighbor to explore

### Characteristics

- No recursion
- Explicit stack
- Better control over memory
- Same logical structure as recursive DFS
- Handles large input without stack overflow

## Key Differences Between the Two Implementations

| Aspect | Recursive DFS | Iterative DFS |
|----------|---------------|---------------|
| DFS style | Recursion | Explicit stack |
| Risk of stack overflow | High | None |
| Memory usage | Higher (call stack) | Lower |
| Scalability | Limited | Much better |
| Stability on large input | Risky | Reliable |
| Clarity | Slightly cleaner | Slightly more complex |

## Why the Iterative Version Is Better

- Python has limited recursion depth
- The graph contains **875k vertices**
- Recursive DFS can exceed stack limits
- Iterative DFS avoids system recursion overhead
- More robust for large-scale graph processing

While the recursive version is more elegant conceptually,  
the iterative version is **far more practical for large datasets**.

## Memory Considerations

This assignment requires careful handling because:

- The graph has nearly 1 million vertices
- Both original and reversed graphs must be stored
- Multiple large arrays must be maintained:
  - `explored`
  - `leader`
  - `order`
- Python recursion depth is limited

Using iterative DFS significantly reduces the risk of memory and stack errors.

## Final Output

The program computes:

- All SCC sizes
- Sorts them in descending order
- Prints the top 5

Example output format:
`[500, 400, 300, 200, 100]`
(Actual values depend on the provided dataset.)

## What This Assignment Demonstrates

- Practical implementation of graph algorithms at scale
- Importance of memory management
- Difference between theoretical O(m + n) complexity and real-world constraints
- Why recursion is sometimes unsuitable for large problems
- The importance of implementation details in performance-critical algorithms
