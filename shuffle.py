class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = 0
        result = []
        while num < n:
            result.append(nums[num])
            result.append(nums[num + n])
            num += 1
        return result
        
# link to question, https://leetcode.com/problems/shuffle-the-array