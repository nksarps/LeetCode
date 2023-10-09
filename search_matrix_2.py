class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            for num in nums:
                if num == target:
                    return True
        return False

# link to question, https://leetcode.com/problems/search-a-2d-matrix-ii/