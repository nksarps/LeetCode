class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 0
        ans = []
        while n < 2:
            for num in nums:
                ans.append(num)
            n += 1
        return ans

# link to question, https://leetcode.com/problems/concatenation-of-array