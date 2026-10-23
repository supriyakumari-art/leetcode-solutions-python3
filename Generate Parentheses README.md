# Generate Parentheses

## 📌 Problem Statement

Given an integer `n`, generate all combinations of `n` pairs of parentheses that are **valid and well-formed**.

A valid combination means:
- Every opening parenthesis `(` has a matching closing parenthesis `)`.
- At no point can closing parentheses exceed opening parentheses.
- The total number of opening and closing parentheses must be equal.


## ⚙️ Approach: DFS and Backtracking

The solution uses Depth-First Search (DFS) to explore all possible combinations of opening and closing parentheses.

### How it works

1. **Initialize the result:** Create an empty list `res` to store valid combinations.
2. **Track parentheses:** `O` represents the remaining opening parentheses, while `C` represents the remaining closing parentheses.
3. **Add an opening parenthesis:** If `O > 0`, add `(` and recursively explore the next state.
4. **Add a closing parenthesis:** If `C > O`, add `)` because a closing parenthesis can only be added when there are more closing parentheses remaining than opening parentheses.
5. **Store the result:** When both `O` and `C` become zero, the generated string is valid and is added to `res`.
6. **Return the result:** Return the list containing all valid combinations.

## 🧪 Example

**Input:**
```python
n = 3
sol = Solution()
print(sol.generateParenthesis(n))
```

**Output:**
```python
['((()))', '(()())', '(())()', '()(())', '()()()']
```

## 📊 Complexity Analysis

- **Time Complexity:** \(O(4^n/\sqrt{n})\) — the number of valid combinations is the \(n\)-th Catalan number. This is a tight bound for generating all combinations when accounting for the output strings.
- **Space Complexity:** \(O(n)\) auxiliary recursion depth, excluding the space required to store the output. The output itself contains \(O(n \cdot C_n)\) characters, where \(C_n\) is the \(n\)-th Catalan number.

## 🎯 Key Concepts

- Recursion
- Depth-First Search (DFS)
- Backtracking
- Catalan Numbers
- String Manipulation

## 🚀 Applications

This problem helps develop an understanding of recursive search and constraint-based generation. Similar techniques are used in expression parsing, balanced-symbol validation, and combinatorial problems.

## 📝 Conclusion

The algorithm efficiently generates every valid combination by building strings one character at a time. By checking the remaining counts before adding parentheses, it avoids exploring invalid combinations and produces only valid results.
