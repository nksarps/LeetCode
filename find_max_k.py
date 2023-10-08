class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_num = 0
        for num in nums:
            if num in nums and -num in nums:
                if num > max_num:
                    max_num = abs(num)
        if max_num == 0:
            return -1
        else:
            return max_num

# link to question, https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/