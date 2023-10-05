class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if sqrt(num).is_integer():
            return True
        return False


# link to question, https://leetcode.com/problems/valid-perfect-square/