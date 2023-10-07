class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        result = num.rstrip('0')
        if not result:
            return 0
        return result

# link to question, https://leetcode.com/problems/remove-trailing-zeros-from-a-string/