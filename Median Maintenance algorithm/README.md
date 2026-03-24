# Median Maintenance Algorithm

The goal of this assignment is to compute the running median of a stream of numbers using an efficient algorithm based on heaps. This problem is a classic example of how appropriate data structures allow us to process data incrementally and efficiently.

## Problem Description

You are given a text file containing 10,000 integers in unsorted order.

The numbers should be treated as a stream, meaning:
- They arrive one by one
- After each new number, you must update the median

### Objective

For each prefix of the stream:

- Let `mₖ` be the median of the first `k` numbers
- Compute the sum: `m₁ + m₂ + m₃ + ... + m₁₀₀₀₀`
- Return: `(sum of medians) mod 10000`

### Median Definition

- If `k` is odd: Median is the middle element
- If `k` is even: Median is the lower median (i.e., the k/2-th smallest element)

---

## Algorithm Overview

The efficient solution uses **two heaps**:

1. **Max-Heap (lower half)**  
   - Stores the smaller half of the numbers  
   - Python uses a min-heap, so values are stored as **negative**

2. **Min-Heap (upper half)**  
   - Stores the larger half of the numbers  

### Key Idea

- Keep both halves balanced so that:
  - `len(lower) == len(upper)` OR
  - `len(lower) == len(upper) + 1`

- The median is always the maximum of the lower half, i.e.: `median = max(lower)`

## Step-by-Step Process

For each incoming number `x`:

1. **Insert into appropriate heap**
   - If `x` is smaller → goes into max-heap (`lower`)
   - Otherwise → goes into min-heap (`upper`)

2. **Rebalance heaps**
   - Ensure size difference is at most 1
   - Move elements between heaps if necessary

3. **Extract median**
   - Median is always the root of the max-heap (`lower`)

4. **Update running sum**

## Time Complexity

- Each insertion: **O(log n)**
- Each rebalance: **O(log n)**
- Total for 10,000 elements: **O(n log n)**

This is efficient enough for streaming large datasets.

## Implementation Details

- Python’s `heapq` is used:
  - Min-heap by default
  - Max-heap simulated using negative values
- The algorithm processes the file line-by-line (streaming approach)
- The final result is computed using modulo: `result % 10000`

## Why This Approach Is Efficient

A naive approach would:
- Re-sort the array after each insertion: **O(n² log n)**

Instead, using two heaps:
- Maintains order dynamically
- Avoids repeated sorting
- Provides constant-time access to the median

## Notes

- The choice of lower median (for even k) is important and required by the assignment
- This problem demonstrates:
  - The power of heap data structures
  - How to handle streaming data efficiently
  - The importance of maintaining invariants (balanced heaps)
