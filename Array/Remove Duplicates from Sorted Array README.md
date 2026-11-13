Remove Duplicates from Sorted Array
Problem Statement

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

The relative order of the elements must be maintained.

Return the number of unique elements k.

The first k elements of nums should contain the unique elements.

Requirement: Solve the problem using O(n) time complexity and O(1) extra space complexity.

Approach: Two Pointers

We use the Two Pointers Technique to remove duplicates from the sorted array without using extra space.

Logic
Initialize a pointer i = 1 to track the position where the next unique element should be placed.
Iterate through the array using pointer j, starting from index 1.
Compare the current element nums[j] with the previous unique element nums[i - 1].
If both elements are different:
Copy nums[j] to nums[i].
Increment i by 1.
If both elements are equal, skip the duplicate.
Return i, which represents the number of unique elements.

Example

Input:

python
nums = [1, 1, 2, 2, 3]


Output:

python
3


Modified Array:

python
[1, 2, 3, 2, 3]


Explanation:

The unique elements are 1, 2, and 3.

Therefore:

Number of unique elements (k) = 3
First 3 elements of the modified array = [1, 2, 3]
Complexity Analysis
Complexity	Value	Explanation
Time Complexity	O(n)	The array is traversed only once.
Space Complexity	O(1)	No additional array or data structure is used.
Key Concepts Used
Two Pointers
Arrays
In-place Modification
Sorted Array
Time and Space Complexity
Conclusion

This solution efficiently removes duplicate elements from a sorted array using the Two Pointers Technique.

It modifies the original array in-place without using extra space.

Time Complexity: O(n)

Space Complexity: O(1)
