class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                nums.append(i)
        return sum(nums)
        
# link to question, https://leetcode.com/problems/sum-multiples/