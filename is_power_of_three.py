class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(100):
            if 3 ** i == n:
                return True
        return False

# link to question, https://leetcode.com/problems/power-of-three/