class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        for i in range(0, 1000):
            if 2 ** i == n:
                count += 1
        if count > 0:
            return True
        else:
            return False
        