class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = floor(len(nums) / 3)
        result = []
        for num in nums:
            if nums.count(num) > check:
                if num in result:
                    pass
                else:
                    result.append(num)
        return result

# link to question, https://leetcode.com/problems/majority-element-ii/