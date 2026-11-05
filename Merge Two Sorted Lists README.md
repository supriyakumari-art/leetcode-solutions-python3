Here is a GitHub-ready README for LeetCode 21 – Merge Two Sorted Lists, following the same format as your previous solution.

Writing

# LeetCode 21: Merge Two Sorted Lists 🔗

**Difficulty:** Easy\
**Topic:** Linked List, Recursion, Two Pointers\
**Language:** Python\
**Problem Link:** [LeetCode - Merge Two Sorted Lists](<https://leetcode.com/problems/merge-two-sorted-lists/>)

## 📌 Problem Description

You are given the heads of two sorted linked lists, `list1` and `list2`.

Merge the two lists into one sorted linked list by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example 1

**Input:**

python

```python
list1 = [1, 2, 4]
list2 = [1, 3, 4]
```

**Output:**

python

```python
[1, 1, 2, 3, 4, 4]
```

### Example 2

**Input:**

python

```python
list1 = []
list2 = []
```

**Output:**

python

```python
[]
```

---

## 💡 Approach: Dummy Node + Two Pointers

We use a dummy node to simplify the process of merging two sorted linked lists.

### Steps:

1. Create a dummy node to act as the starting point of the merged list.
2. Initialize a pointer `cur` at the dummy node.
3. Traverse both linked lists while both have nodes.
4. Compare the values of the current nodes.
5. Attach the smaller node to the merged list.
6. Move the pointer of the list from which the node was selected.
7. Move `cur` to the newly attached node.
8. Once one list becomes empty, attach the remaining nodes of the other list.
9. Return `dummy.next` as the head of the merged linked list.


## 🔍 Dry Run

**Input:**

python

```python
list1 = [1, 2, 4]
list2 = [1, 3, 4]
```

| Iteration | list1.val | list2.val | Selected Node |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 (list1) |
| 2 | 2 | 1 | 1 (list2) |
| 3 | 2 | 3 | 2 (list1) |
| 4 | 4 | 3 | 3 (list2) |
| 5 | 4 | 4 | 4 (list1) |

After the loop, the remaining node from `list2` is attached.

**Final Merged List:**

text

```text
1 → 1 → 2 → 3 → 4 → 4
```

---

## ⚙️ Complexity Analysis

Let:

- `n` = Length of the first linked list.
- `m` = Length of the second linked list.

| Complexity | Value | Explanation |
| --- | --- | --- |
| Time Complexity | O(n + m) | Each node is visited at most once. |
| Space Complexity | O(1) | Only a few extra pointers are used; existing nodes are reused. |

---

## 🧠 Key Concepts Learned

- Linked List Traversal
- Dummy Node Technique
- Two Pointer Approach
- Comparing Node Values
- Merging Sorted Linked Lists
- In-place Linked List Manipulation
- Handling Empty Linked Lists

---

## ✅ Conclusion

This problem demonstrates how to merge two sorted linked lists efficiently using the Dummy Node + Two Pointers approach.

Instead of creating new nodes, we reuse the existing nodes by updating their `next` pointers.

**Time Complexity:** O(n + m)\
**Space Complexity:** O(1)

⭐ If you find this solution helpful, feel free to star this repository\!

Suggested GitHub filename: `LeetCode-21-Merge-Two-Sorted-Lists/README.md`

Suggested commit message: `Add Python solution for LeetCode 21 - Merge Two Sorted Lists`
