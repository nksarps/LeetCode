class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0 
        for num in nums:
            if num == 0:
                pass
            elif num > 0:
                pos += 1
            else:
                neg += 1
        if pos > neg:
            return pos
        return neg

# link to question, https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/