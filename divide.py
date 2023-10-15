class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31
        return int(dividend / divisor)
        
# link to question, https://leetcode.com/problems/divide-two-integers/