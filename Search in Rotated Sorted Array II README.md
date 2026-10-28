Here’s a `README.md` for your solution to LeetCode 81 — Search in Rotated Sorted Array II.

Writing

# Search in Rotated Sorted Array II

## Problem Description

Given an integer array `nums` sorted in non-decreasing order and rotated at an unknown pivot, and an integer `target`, return `True` if `target` exists in the array; otherwise, return `False`.

The array may contain **duplicate elements**.

You must solve the problem while aiming for efficient search performance.

## Examples

### Example 1

**Input:**

python

```
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
```

**Output:**

python

```
True
```

### Example 2

**Input:**

python

```
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
```

**Output:**

python

```
False
```

### Example 3

**Input:**

python

```
nums = [1, 0, 1, 1, 1]
target = 0
```

**Output:**

python

```
True
```

## Approach: Modified Binary Search

We use binary search to locate the target in a rotated sorted array. Since duplicate elements are allowed, we must handle cases where the sorted half cannot be identified immediately.

### Algorithm

1. Initialize two pointers:
   - `left = 0`
   - `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate the middle index using `mid = (left + right) // 2`.
   - If `nums[mid] == target`, return `True`.
   - If `nums[mid] == nums[left]`, increment `left` and continue. This skips an ambiguous duplicate while preserving correctness.
   - If the left half is sorted (`nums[left] <= nums[mid]`):
     - If the target lies within the sorted half, move `right` to `mid - 1`.
     - Otherwise, move `left` to `mid + 1`.
   - Otherwise, the right half is sorted:
     - If the target lies within the right half, move `left` to `mid + 1`.
     - Otherwise, move `right` to `mid - 1`.
3. If the loop finishes without finding the target, return `False`.

## Complexity Analysis

- **Time Complexity:**
  - Average and typical case: `O(log n)`.
  - Worst case: `O(n)`, when duplicates prevent us from determining which half is sorted and we must skip elements one at a time.
- **Space Complexity:** `O(1)`, since the algorithm uses only a constant number of extra variables.

## Key Takeaways

- Modified binary search can efficiently search a rotated sorted array.
- Duplicate elements can make it impossible to identify the sorted half immediately.
- When `nums[mid] == nums[left]`, incrementing `left` helps resolve ambiguity.
- Unlike the version without duplicates, this problem has a worst-case linear time complexity.

## Topics

- Binary Search
- Arrays
- Rotated Sorted Arrays
- Duplicate Elements

## LeetCode

[Search in Rotated Sorted Array II — LeetCode 81](<https://leetcode.com/problems/search-in-rotated-sorted-array-ii/>)
