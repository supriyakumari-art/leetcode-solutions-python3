Find the Duplicate Number
Problem Description

Given an array of integers nums containing n + 1 integers, where each integer is in the range [1, n] inclusive.

There is only one repeated number in the array. Return the repeated number.

Constraints:

Do not modify the input array.
Use only constant extra space.
Solve the problem efficiently.
Approach: Floyd's Cycle Detection Algorithm

We use the Slow and Fast Pointer technique (Tortoise and Hare) to detect a cycle and find its starting point.

Intuition

We treat the array as a linked list:

Each index represents a node.
nums[i] represents the next node.
Since every number is within the range [1, n], every pointer leads to a valid index.

The duplicate number creates a cycle in this linked-list representation.

We use Floyd's Cycle Detection Algorithm to find the entrance of that cycle, which gives us the duplicate number.

Algorithm

Phase 1: Detect the Cycle

Initialize slow and fast pointers at index 0.
Move slow one step at a time: slow = nums[slow].
Move fast two steps at a time: fast = nums[nums[fast]].
Continue until both pointers meet.

Phase 2: Find the Duplicate Number

Reset slow to index 0.
Keep fast at the meeting point.
Move both pointers one step at a time.
When both pointers meet again, the meeting value is the duplicate number.
Code
python

Input:

python
nums = [1, 3, 4, 2, 2]


Output:

python
2


Explanation:

The number 2 appears twice in the array.

By treating the array as a linked list, we detect a cycle and find its entrance, which corresponds to the duplicate number 2.

Complexity Analysis
Complexity	Value	Explanation
Time Complexity	O(n)	Both phases traverse at most a linear number of elements.
Space Complexity	O(1)	Only two pointers are used.
Key Takeaway

Floyd's Cycle Detection Algorithm converts the duplicate number problem into a cycle detection problem.

The algorithm works in two phases:

Detect the cycle using slow and fast pointers.
Find the cycle entrance to identify the duplicate number.

This solution achieves O(n) time complexity and O(1) extra space without modifying the original array.
