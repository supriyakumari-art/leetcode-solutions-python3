Single Element in a Sorted Array
Problem Statement

You are given a sorted array nums in which every element appears exactly twice, except for one element that appears only once.

Your task is to find and return the single element that appears only once.

Requirement: Solve the problem in O(log n) time complexity and O(1) space complexity.

Approach: Binary Search

We use Binary Search to efficiently find the element that appears only once.

Logic
Initialize two pointers:
left = 0
right = len(nums) - 1
Calculate the middle index:
python
mid = (left + right) // 2

Check the pairing pattern:
If mid is odd and nums[mid] == nums[mid - 1], the single element is on the right side.
If mid is even and nums[mid] == nums[mid + 1], the single element is on the right side.
Otherwise, the single element is on the left side or at the middle.
Update the search boundaries:
If the pair is correctly aligned, set left = mid + 1.
Otherwise, set right = mid.
Continue until left == right.
Return nums[left].

Example

Input:

python
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]


Output:

python
2


Explanation:

Every element appears twice except 2, which appears only once. Therefore, the answer is 2.

Complexity Analysis
Complexity	Value	Explanation
Time Complexity	O(log n)	Binary search reduces the search space by half in every iteration.
Space Complexity	O(1)	Only a constant amount of extra space is used.
Key Concepts Used
Binary Search
Array
Index Parity (Even and Odd)
Two Pointers
Time and Space Complexity
Conclusion

This solution efficiently finds the single non-duplicate element using Binary Search. Instead of checking every element, it uses the even-odd index pairing pattern to achieve O(log n) time complexity and O(1) space complexity.
