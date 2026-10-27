# LeetCode 34: Find First and Last Position of Element in Sorted Array

## 📌 Problem Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending positions of a given `target` value.

If the target is not found in the array, return `[-1, -1]`.

**Problem Link:** [LeetCode 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## 💡 Approach: Binary Search

This solution uses **binary search twice** to find the first and last occurrences of the target efficiently.

1. **Find the first occurrence:** When the target is found, save its index and continue searching the left half.
2. **Find the last occurrence:** When the target is found, save its index and continue searching the right half.
3. Return both indices as `[left, right]`.

The helper function `binary_search()` uses the `is_searching_left` parameter to decide which occurrence to find.


## 📊 Example

**Input:**
```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
```

**Output:**
```python
[3, 4]
```

**Explanation:** The target `8` appears at indices `3` and `4`. Therefore, the first occurrence is `3` and the last occurrence is `4`.

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(log n)` — Binary search is performed twice, and each search takes logarithmic time.
- **Space Complexity:** `O(1)` — The algorithm uses only a constant amount of extra space.

## 🛠️ Concepts Used

- Binary Search
- Nested Functions
- Boolean Parameters
- Array Indexing
- Time and Space Complexity

## 🎯 Key Takeaway

By modifying the direction of binary search after finding the target, we can find both the first and last occurrences in **O(log n)** time without scanning the entire array.

---

⭐ If you find this solution helpful, consider giving this repository a star!
