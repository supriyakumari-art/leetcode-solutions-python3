# 3Sum Problem – Python Solution

## 📌 Problem Statement

Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i`, `j`, and `k` are distinct indices.
- The sum of the three elements is equal to `0`.
- The result must not contain duplicate triplets.


## 🧠 Approach: Sorting + Two Pointers

The solution uses sorting and two pointers to find triplets whose sum is zero.

### Step-by-Step Explanation

1. **Initialize a set:** The `ans` set stores unique triplets and prevents duplicate results.
2. **Sort the array:** Sorting makes it easier to adjust the pointers based on the sum.
3. **Fix the first element:** The `for` loop selects the first element of each potential triplet.
4. **Stop early:** If `nums[i] > 0`, stop searching because all remaining elements are also positive.
5. **Use two pointers:** Set `j = i + 1` and `k = n - 1`.
6. **Calculate the sum:** Add `nums[i]`, `nums[j]`, and `nums[k]`.
   - If the sum is `0`, add the triplet to the set and move both pointers.
   - If the sum is greater than `0`, move `k` left to decrease the sum.
   - If the sum is less than `0`, move `j` right to increase the sum.
7. **Return the result:** Convert the stored tuples into lists and return them.

## 🧪 Example

**Input:**

```python
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))
```

**Output:**

```python
[[-1, -1, 2], [-1, 0, 1]]
```

The order of the triplets in the output may vary.

### Explanation

The two unique triplets that sum to zero are:

- `[-1, -1, 2]` → `-1 + (-1) + 2 = 0`
- `[-1, 0, 1]` → `-1 + 0 + 1 = 0`

## ⏱️ Complexity Analysis

- **Time Complexity:** \(O(n^2)\), because the outer loop runs through the array and the two-pointer search takes linear time for each iteration.
- **Space Complexity:** \(O(n)\) auxiliary space for sorting and storing results, excluding implementation-dependent sorting space. The output set can contain \(O(n^2)\) triplets in the worst case.

## 🛠️ Concepts Used

- Arrays and Lists
- Sorting
- Two-Pointer Technique
- Sets and Duplicate Removal
- Time and Space Complexity Analysis

## 🎯 Key Learning

The Two-Pointer Technique reduces the search from a brute-force \(O(n^3)\) approach to \(O(n^2)\). Sorting the array helps move pointers efficiently, while a set ensures that duplicate triplets are not included in the result.

## 🚀 Conclusion

This solution efficiently finds all unique triplets whose sum equals zero. It demonstrates how sorting, two pointers, and sets can work together to solve array problems efficiently.
