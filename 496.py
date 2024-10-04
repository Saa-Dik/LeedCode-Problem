"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above."""
#496. Next Greater Element I:
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Initialize the answer array with -1's, as -1 is the default value if we don't find a next greater element
        ans = [-1] * len(nums1)
        # Map each number to its index in nums1 using enumerate, allowing us to quickly locate the position of a number in nums1
        dic = {num: i for i, num in enumerate(nums1)}
        # Initialize an empty stack, which will help us track numbers in nums2 that are also in nums1 and for which we have not yet found the next greater number
        stack = []
        # Iterate over nums2
        for i in range(len(nums2)):
            curr = nums2[i]
            # If the stack is not empty and the current number is greater than the top of the stack, 
            # this means we have found the next greater element for the num from nums1 on top of the stack
            # We pop this number from the stack and update the corresponding position in the answer array with the current number
            while stack and curr > stack[-1]:
                val = stack.pop()
                ans[dic[val]] = curr
            # If the current number exists in dic (indicating it is common between nums1 and nums2),
            # we add it to the stack for potential future comparison
            if curr in dic:
                stack.append(curr)
        return ans