class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if nums.count(num) == 1:
                unique.append(num)
        return sum(unique) 

# link to question, https://leetcode.com/problems/sum-of-unique-elements/