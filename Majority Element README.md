# Majority Element

## Problem Description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n // 2` times in the array.

You may assume that the majority element always exists in the array.

## Approach: Sorting

1. First, sort the array using `nums.sort()`.
2. Calculate the length of the array using `n = len(nums)`.
3. Return the middle element using `nums[n // 2]`.

### Why does this work?

Since the majority element appears more than `n / 2` times, it must occupy the middle position after sorting the array.

Therefore, `nums[n // 2]` will always be the majority element.

## Example

**Example 1:**

```python
Input: nums = [3, 2, 3]
Output: 3
```

**Example 2:**

```python
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

## Complexity Analysis

- **Time Complexity:** `O(n log n)` – Sorting the array takes O(n log n) time.
- **Space Complexity:** Depends on the sorting implementation. Python's Timsort can use up to O(n) auxiliary space.

## Key Concepts

- Arrays
- Sorting
- Majority Element
- Indexing

## LeetCode

[Majority Element – LeetCode 169](https://leetcode.com/problems/majority-element/)

---

**Language:** Python 3

**Topic:** Array, Sorting
