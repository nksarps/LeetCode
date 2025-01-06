class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, current = nums[0], 0

        for num in nums:
            current = max(num, current + num) 
            maximum = max(maximum, current)

        return maximum

# link https://leetcode.com/problems/maximum-subarray/