# Counting QuickSort Comparisons with different pivot rules

The objective of this assignment is to analyse the **number of comparisons** performed by the QuickSort algorithm under different **pivot selection rules**.

## Problem Overview

You are given a file (`QuickSort.txt`) containing **10,000 distinct integers** between **1 and 10,000**, in unsorted order. Each line corresponds to one element of the input array.

The task is to compute the **total number of comparisons** made by QuickSort when sorting this array, using three different pivot selection strategies.

## Important Rules

- You must not count comparisons one by one.
- For each recursive call on a subarray of length `m`, you should:
  - Add **`m - 1` comparisons** to the total.
- The **Partition subroutine must be implemented exactly as described in the video lectures**.
- No credit is given for alternative partition implementations, even if logically equivalent.


## Shared Partition Function

All three problems use the same Partition subroutine, implemented exactly as shown in the lectures:

```python
def partition(array, low, high):
    pivot = array[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1
```

### Problems breakdown
#### Problem 1 — First Element as Pivot
- **Pivot Rule:** Always use the first element of the (sub)array as the pivot.
- **Notes**:
  - This approach performs poorly on nearly sorted or reverse-sorted arrays.
  - No pivot swapping is required before partitioning.

#### Problem 2 — Final Element as Pivot
- **Pivot Rule:** Always use the last element of the array as the pivot.
- **Important Detail**:
  - Before calling partition, the last element must be swapped with the first element, so that the partition subroutine works as expected.

#### Problem 3 — Median-of-Three Pivot
- **Pivot Rule:** Choose the pivot as the median of:
  - **First element**
  - **Middle element**: For an array of length m:
    - If `m` is odd → the middle element is clear
    - If `m` is even (`2k`) → use the `k`-th element (1-based indexing)
  - **Last element**
- Do NOT count comparisons used to identify the median.
- As with the other problems, simply add `m - 1` comparisons per recursive call.

## Key Takeaways
- The number of comparisons in QuickSort depends heavily on pivot choice.
- Poor pivot selection can degrade performance to O(n²).
- Smarter pivot rules (like median-of-three) significantly improve performance on real-world data.
