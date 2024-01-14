class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total_numbers = high - low + 1
        if total_numbers % 2 == 0:
            return total_numbers // 2
        else:
            return (total_numbers // 2) + (low % 2)

# link to question, https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/