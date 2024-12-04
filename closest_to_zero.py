class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_diff = min(abs(num) for num in nums)
        closest_nums = [num for num in nums if abs(num) == min_diff]
        return max(closest_nums)

#link: https://leetcode.com/problems/find-closest-number-to-zero/description/