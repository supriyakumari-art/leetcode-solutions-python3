Find Peak Element
Problem Description

Given an integer array nums, find a peak element and return its index.

A peak element is an element that is strictly greater than its neighbors.

For an element at the boundary, only its existing neighbor is considered.
You may assume that nums[-1] = nums[n] = -∞.
The solution should run in O(log n) time complexity.
Approach: Binary Search

We use Binary Search to efficiently find a peak element.

Algorithm
Initialize two pointers:
left = 0
right = len(nums) - 1
Run a binary search while left < right.
Calculate the middle index using an upper-middle approach:
python
mid = left + (right - left + 1) // 2

Compare nums[mid] with its previous element:
If nums[mid] < nums[mid - 1], the sequence is descending, so a peak must exist on the left side. Update right = mid - 1.
Otherwise, a peak exists at mid or somewhere on the right side. Update left = mid.
When left == right, return left as the peak index.
Code
python

Example

Input:

python
nums = [1, 2, 3, 1]


Output:

python
2


Explanation:

The element 3 at index 2 is greater than its neighbors 2 and 1.

Therefore, index 2 is a peak element.

Complexity Analysis
Complexity	Value	Explanation
Time	O(log n)	Search space is reduced by approximately half in each iteration.
Space	O(1)	Only a constant amount of extra space is used.
Key Takeaway

Binary Search can find a peak element without checking every array element.

By comparing the middle element with its previous element, we determine which direction contains a peak and eliminate half of the search space in every iteration.
