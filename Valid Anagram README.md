# Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

## Approach: Hash Map / Frequency Counter

- Import `Counter` from Python's `collections` module.
- `Counter(s)` counts the frequency of each character in string `s`.
- `Counter(t)` counts the frequency of each character in string `t`.
- Compare both frequency counters.
- If both counters are equal, return `True`; otherwise, return `False`.

## Example

**Example 1:**

```python
Input: s = "anagram", t = "nagaram"
Output: True
```

**Explanation:** Both strings contain the same characters with the same frequencies.

**Example 2:**

```python
Input: s = "rat", t = "car"
Output: False
```

**Explanation:** The character frequencies are different.

## Complexity Analysis

- **Time Complexity:** `O(n)` – Counting the characters in both strings takes linear time.
- **Space Complexity:** `O(k)` – Where `k` is the number of distinct characters stored in the Counter.

## Key Concepts
- Hash Maps
- Character Frequency Counting
- Python Collections
- String Manipulation

## LeetCode
[Valid Anagram – LeetCode 242](https://leetcode.com/problems/valid-anagram/)

---
**Language:** Python 3

**Topic:** Strings, Hash Map
