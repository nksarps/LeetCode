class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for num in nums:
            if not max(nums) == num and not min(nums) == num:
                return num
        return -1
        

# link to question, https://leetcode.com/problems/neither-minimum-nor-maximum/