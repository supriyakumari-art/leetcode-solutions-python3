Here is a GitHub-ready `README.md` for your Python solution to LeetCode 101 – Symmetric Tree.

Writing

# 🌳 Symmetric Tree – LeetCode 101

## 📌 Problem Description

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

A binary tree is symmetric if its left and right subtrees are mirror images of each other.

**Example 1:**

text

```text
       1
      / \
     2   2
    / \ / \
   3  4 4  3
```

**Output:**

python

```python
True
```

**Example 2:**

text

```text
       1
      / \
     2   2
      \   \
       3   3
```

**Output:**

python

```python
False
```

## 💡 Approach: Recursive DFS

The solution uses **recursion (Depth-First Search)** to compare the left and right subtrees.

Two subtrees are mirror images if:

1. Both nodes are `None`.
2. If only one node is `None`, they are not symmetric.
3. Both nodes have the same value.
4. The left child of the first tree matches the right child of the second tree.
5. The right child of the first tree matches the left child of the second tree.

### 🔍 Algorithm

1. If the root is `None`, return `False` (as implemented in this solution).
2. If both children of the root are `None`, return `True`.
3. If only one child exists, return `False`.
4. Define a recursive helper function `check(p, q)`:
   - If both nodes are `None`, return `True`.
   - If one node is `None` or their values differ, return `False`.
   - Recursively compare opposite children.
5. Return the result of comparing the root's left and right subtrees.

## ⏱️ Complexity Analysis

Let `N` be the number of nodes in the binary tree.

- **Time Complexity:** `O(N)` – Each node is visited at most once.
- **Space Complexity:** `O(H)` – Recursion stack space, where `H` is the height of the tree.
  - Balanced tree: `O(log N)`
  - Skewed tree: `O(N)`

## 🧠 Key Concepts

- Binary Trees
- Recursion
- Depth-First Search (DFS)
- Tree Traversal
- Mirror Trees

## 🔗 Problem Link

[LeetCode 101 – Symmetric Tree](<https://leetcode.com/problems/symmetric-tree/>)

---

⭐ If you find this solution helpful, feel free to star the repository\!

Small note: Your code returns `False` for an empty tree (`root = None`). LeetCode's standard expected behavior is `True` for an empty tree. To match the problem definition, change:

python

```python
if not root:
    return False
```

to:

python

```python
if not root:
    return True
```
