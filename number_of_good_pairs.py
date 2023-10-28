class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for count in range(len(nums)):
            for num in range(count+1, len(nums)):
                if nums[count] == nums[num]:
                    result += 1
        return result 
        
# link to question, https://leetcode.com/problems/number-of-good-pairs/