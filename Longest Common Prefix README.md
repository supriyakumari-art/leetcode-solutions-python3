Longest Common Prefix
Problem Description

Given an array of strings strs, find the longest common prefix string amongst all the strings.

If there is no common prefix, return an empty string "".

Approach: Horizontal Character Comparison

The solution uses a character-by-character comparison approach.

Check if the input list is empty. If so, return "".
Iterate through each character of the first string.
Compare the current character with the corresponding character in every other string.
If a mismatch is found or a string ends, return the prefix up to that index.
If all characters match, return the first string.

Examples

Example 1:

python
Input: strs = ["flower", "flow", "flight"]
Output: "fl"


Example 2:

python
Input: strs = ["dog", "racecar", "car"]
Output: ""


Example 3:

python
Input: strs = ["interview", "internet", "internal"]
Output: "inter"

Complexity Analysis
Time Complexity: O(N × M)
N = Number of strings.
M = Length of the first string (maximum characters checked per string).
Space Complexity: O(1)
Uses constant extra space, excluding the returned prefix.
Key Concepts
String Manipulation
Nested Loops
Character Comparison
Prefix Matching
LeetCode

Problem: Longest Common Prefix

Difficulty: Easy

⭐ If you find this solution helpful, consider giving this repository a star!
