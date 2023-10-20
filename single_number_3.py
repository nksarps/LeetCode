class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums.count(num) == 1:
                result.append(num)
                if len(result) == 2:
                    return result 


# link to question, https://leetcode.com/problems/single-number-iii/