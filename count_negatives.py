class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for nums in grid:
            for num in nums:
                if num < 0:
                    result += 1
        return result 


# link to question, https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/