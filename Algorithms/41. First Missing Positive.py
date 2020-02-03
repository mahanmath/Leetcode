class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L = len(nums)
        nums = set(nums)
        for i in range(1, L + 2):
            if(not i in nums):
                return i