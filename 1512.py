"""Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j."""

# 1512. Number of Good Pairs

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count = count + 1
            pairs += count
        return pairs
        

