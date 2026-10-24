# Letter Combinations of a Phone Number 📱

## 📌 Problem Description

Given a string containing digits from `2` to `9`, return all possible letter combinations that the number could represent.

The mapping of digits to letters is the same as on a traditional telephone keypad. Note that `1` does not map to any letters.

If the input string is empty, return an empty list.

**LeetCode Problem:** [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)


## ⚙️ Approach

This solution uses **Backtracking** to generate every possible letter combination.

1. **Handle empty input:** If `digits` is empty, return `[]`.
2. **Create the keypad mapping:** Store the letters corresponding to each digit from `2` to `9`.
3. **Initialize variables:** `ans` stores the final combinations, while `path` stores the current combination being built.
4. **Explore combinations:** The `backtrack(index)` function iterates through every letter mapped to the current digit.
5. **Build the combination:** Add a letter to `path` and recursively process the next digit.
6. **Backtrack:** Remove the
