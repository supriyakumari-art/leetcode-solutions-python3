# Permutations – Python Solution

## 📌 Problem Statement

Given an array of distinct integers `nums`, return all possible permutations of the elements.

A permutation is a rearrangement of all the elements in a particular order.

## 🧠 Approach: Recursion and Backtracking

This solution uses recursion and backtracking to generate all possible arrangements of the given elements.

### Step-by-Step Explanation

1. **Initialize the result:** Create an empty list `res` to store all permutations.
2. **Define the recursive function:** The function `perms(i)` generates permutations by fixing elements one position at a time.
3. **Base case:** When `i == len(nums)`, all positions are filled. Append a copy of the current arrangement to `res`.
4. **Swap elements:** The loop selects each remaining element and swaps it with the element at index `i`.
5. **Recursive call:** Call `perms(i + 1)` to generate arrangements for the next position.
6. **Backtrack:** Swap the elements back to restore the original arrangement before trying another choice.
7. **Return the result:** Return `res`, which contains all generated permutations.

## 🧪 Example

**Input:**

```python
nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))
```

**Output:**

```python
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 2, 1],
    [3, 1, 2]
]
```

## 🔍 How Backtracking Works

For the input `[1, 2, 3]`:

- First, the algorithm fixes `1` and generates permutations of `[2, 3]`.
- Next, it fixes `2` and generates permutations of `[1, 3]`.
- Finally, it fixes `3` and generates permutations of `[2, 1]`.

After each recursive call, the swap is undone. This allows the algorithm to explore other arrangements without
