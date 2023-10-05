class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(100):
            if 4 ** i == n:
                return True
        return False

# link to question, https://leetcode.com/problems/power-of-four/
