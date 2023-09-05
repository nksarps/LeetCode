class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2 
        actual_sum = sum(nums) 

        if n == 0:
            return 0 

        return expected_sum - actual_sum
        