class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num = max(nums)
        return nums.index(num) 

# link to question, https://leetcode.com/problems/find-peak-element/