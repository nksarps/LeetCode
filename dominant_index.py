class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
        for num in nums:
            if num != maximum:
                if not num * 2 <= maximum:
                    return -1
        return nums.index(maximum)
        
# link to question, https://leetcode.com/problems/largest-number-at-least-twice-of-others/