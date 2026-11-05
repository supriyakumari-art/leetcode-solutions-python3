Here is a GitHub-ready `README.md` for your LeetCode solution, with problem description, approach, code, dry run, and complexity analysis.

Writing

# LeetCode 2: Add Two Numbers 🧮

**Difficulty:** Medium\
**Topic:** Linked List, Math\
**Language:** Python\
**Problem Link:** [LeetCode - Add Two Numbers](<https://leetcode.com/problems/add-two-numbers/>)

## 📌 Problem Description

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list, also in reverse order.

### Example

**Input:**

python

```python
l1 = [2, 4, 3]
l2 = [5, 6, 4]
```

**Output:**

python

```python
[7, 0, 8]
```

**Explanation:**

- First linked list represents 342.
- Second linked list represents 465.
- Their sum is 342 + 465 = 807.
- The result in reverse order is `[7, 0, 8]`.

---

## 💡 Approach: Dummy Node + Carry

The solution uses a dummy node and carry-based addition, similar to normal mathematical addition.

### Steps:

1. Create a dummy node to simplify linked list construction.
2. Initialize `carry = 0`.
3. Traverse both linked lists simultaneously.
4. Add the current values of both nodes and the carry.
5. Calculate the digit using `total % 10`.
6. Calculate the carry using `total // 10`.
7. Create a new node with the calculated digit.
8. Move to the next nodes.
9. Continue until both lists are exhausted and carry becomes zero.
10. Return `dummy.next` as the final linked list.

## 🔍 Dry Run

**Input:**

python

```python
l1 = [2, 4, 3]
l2 = [5, 6, 4]
```

| Iteration | Calculation | Digit | Carry |
| --- | --- | --- | --- |
| 1 | 2 + 5 + 0 = 7 | 7 | 0 |
| 2 | 4 + 6 + 0 = 10 | 0 | 1 |
| 3 | 3 + 4 + 1 = 8 | 8 | 0 |

**Result:**

text

```text
7 → 0 → 8
```

---

## ⚙️ Complexity Analysis

Let:

- `n` = Length of the first linked list.
- `m` = Length of the second linked list.

| Complexity | Value | Explanation |
| --- | --- | --- |
| Time | O(max(n, m)) | Each node is visited once. |
| Space | O(max(n, m)) | Extra space for the resulting linked list. |

---

## 🧠 Key Concepts Learned

- Linked List Traversal
- Dummy Node Technique
- Carry Handling
- Integer Division (`//`)
- Modulus Operator (`%`)
- Handling Unequal Linked List Lengths
- Edge Case Handling

### Important Edge Case

**Input:**

python

```python
l1 = [9, 9]
l2 = [1]
```

**Output:**

python

```python
[0, 0, 1]
```

This handles the remaining carry after both linked lists are exhausted.

---

## ✅ Conclusion

This problem demonstrates how to perform addition using linked lists without converting them into normal integers.

The Dummy Node + Carry technique makes the implementation clean, efficient, and easy to understand.

**Time Complexity:** O(max(n, m))\
**Space Complexity:** O(max(n, m))

---

⭐ If you find this solution helpful, feel free to star this repository\!

Suggested GitHub filename: `LeetCode-2-Add-Two-Numbers/README.md`

Suggested repository description: `My Python solutions to LeetCode problems with explanations, approaches, dry runs, and complexity analysis.`
