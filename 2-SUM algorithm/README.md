# 2-SUM Algorithm

The goal of this assignment is to compute how many target values `t` within a given range can be formed by the sum of two distinct numbers from a large dataset.

This problem highlights the importance of hashing, sorting, and efficient search techniques when working with large-scale data.

## Problem Description

You are given a text file containing **1,000,000 integers**:
- Integers can be **positive or negative**
- Some values may be **repeated**

### Objective

Compute the number of target values `t` in the interval: `[-10000, 10000]`
such that there exist **distinct numbers** `x` and `y` in the array satisfying `x + y = t`

`x` and `y` must be **distinct numbers** (i.e., `x ≠ y`)

## Algorithm Overview

The core idea of the 2-SUM problem is:

1. Iterate through the dataset
2. Check whether a complementary value exists such that:
   `y = t - x`
3. Count how many valid target values `t` can be formed

---

## Approach Overview

Out of curiosity and experimentation, I implemented **two different approaches**:

### Version 1 — Hash Set + Full Target Scan

- Converts the input array into a **set** for O(1) lookups
- Iterates through:
  - Every number `x`
  - Every possible target `t` in [-10000, 10000]
- Checks if `y = t - x` exists in the set

#### Characteristics
- Very simple and intuitive
- Direct implementation of the problem definition
- Uses hashing effectively
- **Major drawback:** unnecessary repeated work

#### Time Complexity
- O(n * k), where:
  - `n = number of elements` (~1,000,000)
  - `k = number of targets` (20,001)

### Version 2 — Sorting + Binary Search (Optimised)

- Removes duplicates and sorts the array
- For each number `x`, computes the **valid range of y values** such that:

  `-10000 ≤ x + y ≤ 10000`

- Uses the `bisect` module to:
  - Find the lower bound (`bisect_left`)
  - Find the upper bound (`bisect_right`)
- Only iterates over values within this valid range

#### Characteristics
- Much more efficient
- Avoids checking impossible combinations
- Uses binary search to reduce search space
- Still ensures distinct values (`x ≠ y`)

#### Time Complexity
- Sorting: O(n log n)
- Main loop: significantly reduced compared to Version 1

## Performance Comparison

| Method | Approach | Time Complexity | Time Taken |
|--------|----------|----------------|------------|
| Version 1 | Hash Set + Full Scan | O(n * k) | **+10 minutes** |
| Version 2 | Sorting + Binary Search | ~O(n log n) | **~3 seconds** |

## Key Differences Between the Two Implementations

| Aspect | Version 1 (Hash Set) | Version 2 (Binary Search) |
|--------|---------------------|----------------------------|
| Data structure | Set | Sorted list |
| Strategy | Check all targets for each x | Restrict valid range of y |
| Search method | Direct lookup | Binary search (`bisect`) |
| Work done | Redundant and repeated | Focused and minimal |
| Performance | Very slow | Very fast |
| Scalability | Poor | Good |

## Why Version 2 Is Better

- **Reduces search space dramatically** by only considering valid `y` values
- Avoids looping through all 20,001 targets for every number
- Leverages **binary search**, which is much faster than brute-force scanning
- Eliminates unnecessary computations
- Scales efficiently to very large datasets (1M+ elements)

Version 1 is useful for understanding the problem.  
Version 2 is the practical, scalable solution.

## Notes

- Using a `set` ensures fast lookups but does not guarantee efficiency if the search space is too large.
- Sorting combined with binary search is a powerful technique for reducing unnecessary work.
- This problem demonstrates:
  - The importance of algorithmic thinking
  - How constraints can guide optimisation
  - The difference between a working solution and a scalable one
- The `bisect` module is especially useful for:
  - Range queries in sorted arrays
  - Efficient boundary searches
