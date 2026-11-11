# Maximum Subarray

## Problem Description

Given an integer array `nums`, find the subarray with the largest sum and return its sum.

A subarray is a contiguous part of an array containing at least one element.

## Approach: Kadane's Algorithm

We use **Kadane's Algorithm** to find the maximum subarray sum efficiently.

### Steps

1. Initialize `maxSum` with the first element of the array.
2. Initialize `currentSum` with the first element.
3. Traverse the array starting from the second element.
4. For each element, decide whether to:
   - Start a new subarray from the current element.
   - Extend the previous subarray by adding the current element.
5. Update `maxSum` whenever a larger sum is found.
6. Return `maxSum`.

## Example

**Input:**
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output:**
```python
6
```

**Explanation:**

The subarray `[4, -1, 2, 1]` has the largest sum.

Maximum Sum = `4 + (-1) + 2 + 1 = 6`.

## Complexity Analysis

- **Time Complexity:** O(n) – We traverse the array only once.
- **Space Complexity:** O(1) – We use only two extra variables.

## Key Concepts

- Array
- Dynamic Programming
- Kadane's Algorithm
- Greedy Approach

## LeetCode

[Maximum Subarray – LeetCode 53](https://leetcode.com/problems/maximum-subarray/)

---

**Author:** Supriya Kumari
