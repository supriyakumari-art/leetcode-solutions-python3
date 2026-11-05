Here is a GitHub-ready README for LeetCode 66 – Plus One, following the same format as your previous solutions.

Writing

# LeetCode 66: Plus One ➕

**Difficulty:** Easy\
**Topic:** Array, Math\
**Language:** Python\
**Problem Link:** [LeetCode - Plus One](<https://leetcode.com/problems/plus-one/>)

## 📌 Problem Description

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer.

The digits are ordered from most significant to least significant, from left to right.

Increment the large integer by one and return the resulting array of digits.

### Example 1

**Input:**

python

```python
digits = [1, 2, 3]
```

**Output:**

python

```python
[1, 2, 4]
```

**Explanation:**

The array represents the number 123. Adding one gives 124.

### Example 2

**Input:**

python

```python
digits = [4, 3, 9]
```

**Output:**

python

```python
[4, 4, 0]
```

**Explanation:**

439 + 1 = 440.

### Example 3

**Input:**

python

```python
digits = [9, 9, 9]
```

**Output:**

python

```python
[1, 0, 0, 0]
```

**Explanation:**

999 + 1 = 1000.

---

## 💡 Approach: Reverse Traversal + Carry Handling

We traverse the array from right to left because addition starts from the last digit (ones place).

### Steps:

1. Start iterating from the last index using `range(len(digits)-1, -1, -1)`.
2. Check whether the current digit is 9.
3. If the digit is 9:
   - Change it to 0.
   - Continue to the previous digit because a carry is generated.
4. If the digit is not 9:
   - Increment it by 1.
   - Return the updated array immediately.
5. If all digits are 9, prepend 1 to the array and return the result.

## 🔍 Dry Run

### Example 1

**Input:**

python

```python
digits = [1, 2, 3]
```

| Index | Current Digit | Operation | Result |
| --- | --- | --- | --- |
| 2 | 3 | 3 + 1 | \[1, 2, 4\] |

The digit is not 9, so we increment it and return immediately.

**Output:**

python

```python
[1, 2, 4]
```

### Example 2

**Input:**

python

```python
digits = [1, 2, 9]
```

| Index | Current Digit | Operation | Result |
| --- | --- | --- | --- |
| 2 | 9 | Change to 0 | \[1, 2, 0\] |
| 1 | 2 | Increment by 1 | \[1, 3, 0\] |

**Output:**

python

```python
[1, 3, 0]
```

### Example 3: Edge Case

**Input:**

python

```python
digits = [9, 9, 9]
```

| Index | Current Digit | Operation | Result |
| --- | --- | --- | --- |
| 2 | 9 | Change to 0 | \[9, 9, 0\] |
| 1 | 9 | Change to 0 | \[9, 0, 0\] |
| 0 | 9 | Change to 0 | \[0, 0, 0\] |

All digits are 9, so we execute:

python

```python
return [1] + digits
```

**Output:**

python

```python
[1, 0, 0, 0]
```

---

## ⚙️ Complexity Analysis

Let `n` be the length of the input array.

| Complexity | Value | Explanation |
| --- | --- | --- |
| Time Complexity | O(n) | In the worst case, we traverse all digits. |
| Space Complexity | O(n) | In the worst case, a new array is created when all digits are 9. |

The algorithm modifies the original array in place for most cases.

---

## 🧠 Key Concepts Learned

- Array Traversal
- Reverse Iteration
- Carry Handling
- Conditional Statements
- Python `range()` Function
- List Concatenation
- Edge Case Handling

---

## ✅ Conclusion

This problem demonstrates how to perform addition on an integer represented as an array without converting the entire array into an integer.

The reverse traversal approach efficiently handles carry propagation and avoids unnecessary integer conversions.

**Time Complexity:** O(n)\
**Space Complexity:** O(n) worst case

⭐ If you find this solution helpful, feel free to star this repository\!

Suggested GitHub filename: `LeetCode-66-Plus-One/README.md`

Suggested commit message: `Add Python solution for LeetCode 66 - Plus One`
