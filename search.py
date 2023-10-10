class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        count = 0
        if not target in nums: 
            return -1
        else:
            while count < len(nums):
                if nums[count] == target:
                    index = count
                    return index
                count += 1

# link to question, https://leetcode.com/problems/binary-search/