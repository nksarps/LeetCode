class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_numbers = set(range(1, n+1))
        missing_numbers = list(all_numbers - set(nums))
        return missing_numbers

# link to question, https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/