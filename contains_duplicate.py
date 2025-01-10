class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        

# link to question, https://leetcode.com/problems/contains-duplicate/