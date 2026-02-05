# Counting Inversions via Merge Sort

The goal of this assignment is to compute the number of **inversions** in a large array using an efficient divide-and-conquer approach.

## Problem Description

You are given a text file containing **100,000 distinct integers**, each between **1 and 100,000**, arranged in an arbitrary order.
Each line of the file corresponds to one element of the array.

An **inversion** is defined as a pair of indices `(i, j)` such that:

- `i < j`
- `A[i] > A[j]`

### Objective

Compute the **total number of inversions** in the array. Because of the size of the input, a **fast divide-and-conquer algorithm** (based on Merge Sort) is required.

---

## Approach Overview

Out of curiosity, I implemented **two different methods** to solve the problem:

### Method 1 — Brute Force (Naive Approach)
- Compares every pair of elements
- Simple to understand but extremely slow
- **Time complexity**: O(n²)

### Method 2 — Divide and Conquer (Merge Sort)
- Counts inversions during the merge step
- Efficient and scalable
- **Time complexity**: O(n log n)

Both methods return the **same correct result**, but with dramatically different performance.

## Performance Comparison

These are the results I got from performing both codes.

| Method | Time Complexity | Time taken (sorting 10,000 elements) | Result |
|------|----------------|------------------------|--------|
| Brute Force | O(n²) | 5 min 49 sec | 2407905288 |
| Merge Sort | O(n log n) | ~1 sec | 2407905288 |

## Final Answer
2407905288 (this is the value submitted on edX), specific to the text file provided.

### Notes
- The brute-force approach is useful for validation on small inputs, but completely impractical for large datasets.
- The merge sort approach demonstrates how divide-and-conquer techniques dramatically improve performance.
- This problem is a classic example of why asymptotic analysis matters in real-world computing.
