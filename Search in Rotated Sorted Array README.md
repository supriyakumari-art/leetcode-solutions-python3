Find Minimum in Rotated Sorted Array
Problem Description

Given an array of unique integers nums that was originally sorted in ascending order and then rotated at an unknown pivot, return the minimum element of the array.

You must write an algorithm that runs in O(log n) time.

Example 1

Input:

python
nums = [3, 4, 5, 1, 2]


Output:

python
1


Explanation: The original sorted array [1, 2, 3, 4, 5] was rotated. The minimum element is 1.

Example 2

Input:

python
nums = [4, 5, 6, 7, 0, 1, 2]


Output:

python
0


Explanation: The minimum element in the rotated array is 0.

Example 3

Input:

python
nums = [11, 13, 15, 17]


Output:

python
11


Explanation: The array has not been rotated, so the first element is the minimum.

Approach: Binary Search

We use binary search to find the minimum element efficiently.

Algorithm
Initialize two pointers:
left = 0
right = len(nums) - 1
While left < right:
Calculate the middle index: mid = (left + right) // 2.
If nums[mid] <= nums[right], the minimum lies in the left half, including mid. Set right = mid.
Otherwise, the minimum lies in the right half, excluding mid. Set left = mid + 1.
When left == right, both pointers indicate the minimum element.
Return nums[left].


Complexity Analysis
Time Complexity: O(log n) — Binary search eliminates approximately half of the remaining search space in each iteration.
Space Complexity: O(1) — The algorithm uses only a constant number of extra variables.
Key Takeaway

Binary search works because the rotated sorted array contains enough ordering information to determine which half may contain the minimum. Comparing nums[mid] with nums[right] allows us to narrow the search efficiently without checking every element.

Topics
Binary Search
Arrays
Rotated Sorted Arrays
LeetCode

Find Minimum in Rotated Sorted Array — LeetCode 153
