class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = list(set(nums))

        if len(distinct_nums) < 3:
            return max(distinct_nums)

        distinct_nums.sort(reverse=True)
        
        return distinct_nums[2]
        
# link to question, https://leetcode.com/problems/third-maximum-number/