# 350. Intersection of Two Arrays II

"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order."""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i) #akn amra remove use korci karon amar nums2 ar element i rakho and num2 ar element gula remove kore dao
        return result


        