class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start = 0
        result = []
        while start < n:
            result.append(nums[start])
            result.append(nums[start + n])
            start += 1
        return result
        
# link to question, https://leetcode.com/problems/shuffle-the-array/