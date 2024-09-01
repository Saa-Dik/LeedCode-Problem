# 349. Intersection of Two Arrays

"""Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order."""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in  nums1:
            if i in nums2 and i not in result: #and i not in result: ati use korar karon amra output a akoi number jeno ektar besi nah ase
                result.append(i)
        return result