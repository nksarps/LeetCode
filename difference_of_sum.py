class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            while not num == 0:
                last_num = num % 10
                digit_sum += last_num
                num //= 10
        return abs(element_sum - digit_sum)
        
# link to question, https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/