class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        result = 0
        for num in range(1, max_num+1):
            if min_num % num == 0 and max_num % num == 0:
                if num > result:
                    result = num
        return result 

# link to question, https://leetcode.com/problems/find-greatest-common-divisor-of-array/