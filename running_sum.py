class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n-1, -1, -1):
            sum = 0
            for j in range(i, -1, -1):
                sum += nums[j]
            result.append(sum)
        return result[::-1]

#link: https://leetcode.com/problems/running-sum-of-1d-array/