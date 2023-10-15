class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        count = 0
        for num in nums:
            for num_again in nums:
                if num_again < num:
                    count += 1
            result.append(count)
            count = 0
        return result 

# link to question, https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/