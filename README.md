# Search in Rotated Sorted Array 🔍

## 📌 Problem Description

Given an integer array `nums` sorted in ascending order with **distinct values**, the array may have been rotated at an unknown pivot.

Given an integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

The solution must run in **\(O(\log n)\) time complexity**.

**LeetCode Problem:** [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## ⚙️ Approach

This solution uses **Modified Binary Search** to search efficiently in a rotated sorted array.

1. **Initialize pointers:** Set `left` to the first index and `right` to the last index.
2. **Find the middle:** Calculate `mid = (left + right) // 2`.
3. **Check the target:** If `nums[mid] == target`, return `mid`.
4. **Identify the sorted half:** Determine whether the left or right half is sorted.
5. **Narrow the search:**
   - If the left half is sorted, check whether the target lies within that half.
   - Otherwise, the right half is sorted; check whether the target lies within it.
6. **Update pointers:** Discard the half that cannot contain the target.
7. **Return the result:** If the target is not found, return `-1`.

## 🧪 Examples

### Example 1

**Input**
```text
nums = [4,5,6,7,0,1,2]
target = 0
```

**Output**
```text
4
```

**Explanation:** The target `0` is located at index `4`.

### Example 2

**Input**
```text
nums = [4,5,6,7,0,1,2]
target = 3
```

**Output**
```text
-1
```

**Explanation:** The target `3` does not exist in the array.

### Example 3

**Input**
```text
nums = [1]
target = 0
```

**Output**
```text
-1
```

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(log n)` — the search space is approximately halved in each iteration.
- **Space Complexity:** `O(1)` — the algorithm uses only a
