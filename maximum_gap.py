class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_diff = 0
        nums.sort()
        if len(nums) < 2:
            return 0 
        for n in range(len(nums)):
            if not n == len(nums) - 1:
                diff = abs(nums[n] - nums[n+1])
                if diff > max_diff:
                    max_diff = diff
        return max_diff

# link to question, https://leetcode.com/problems/maximum-gap/