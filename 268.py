class Solution:
    def missingNumber(self, nums: List[int])-> int:
        n = len(nums)
        find_num = n * (n+1) // 2
        value = sum(nums)
        miss_value = find_num - value
        return miss_value