class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation = bin(n)
        return binary_representation.count('1')

# link to question, https://leetcode.com/problems/number-of-1-bits/