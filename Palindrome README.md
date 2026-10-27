# Palindrome Number | LeetCode 9

A Python solution to **LeetCode Problem 9: Palindrome Number**, using an optimized mathematical approach to check whether an integer reads the same forward and backward.

## 📌 Problem Statement

Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A palindrome is a number that remains the same when its digits are reversed.

### Examples

| Input | Output | Explanation |
|---|---|---|
| `x = 121` | `True` | Reads the same forward and backward |
| `x = -121` | `False` | Negative numbers are not palindromes |
| `x = 10` | `False` | Reversed number would be `01` |
| `x = 0` | `True` | Zero is a palindrome |

## 💡 Approach: Reverse Half of the Number

Instead of converting the integer into a string, this solution reverses only half of its digits. This reduces unnecessary work and achieves **O(1) auxiliary space complexity**.

### Algorithm

1. Return `False` if the number is negative.
2. Return `False` if the number ends in zero but is not zero itself.
3. Initialize `reversed_half = 0`.
4. Extract the last digit using `x % 10`.
5. Append that digit to `reversed_half` and remove it from `x` using integer division.
6. Continue until the reversed half is greater than or equal to the remaining half.
7. Compare the two halves. For odd-length numbers, ignore the middle digit.

## 🔍 Example Walkthrough

**Input:** `x = 1221`

| Step | `x` | `reversed_half` |
|---|---:|---:|
| Initial | 1221 | 0 |
| 1 | 122 | 1 |
| 2 | 12 | 12 |

The remaining half and the reversed half are equal.

**Output:** `True`

## ⏱️ Complexity Analysis

Let `n` be the number of digits in the input.

- **Time Complexity:** `O(log x)` for positive integers, equivalently `O(n)` in terms of the number of digits. The algorithm processes approximately half the digits.
- **Auxiliary Space Complexity:** `O(1)` because only a constant number of variables are used.

## 🧠 Key Concepts

- Integer arithmetic
- Modulo operator (`%`)
- Floor division (`//`)
- While loops
- Number manipulation
- Time and space complexity optimization

## 📚 What I Learned

- How to check palindromes without string conversion.
- How to extract and reverse digits using mathematical operations.
- How to optimize an algorithm for constant auxiliary space.
- How to handle negative numbers and trailing zeros.

## 🏷️ Technologies

`Python` `LeetCode` `Algorithms` `Math` `DSA`

## 🔗 Reference

[LeetCode — Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

**Author:** Supriya Kumari
