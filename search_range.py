class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        count = 0 
        n = 0
        current = 0
        if not target in nums:
            return [-1, -1]
        elif nums.count(target) == 1:
            for n in range(len(nums)):
                if nums[n] == target:
                    return [n, n]
        else:
            for n in range(len(nums)):
                if nums[n] == target:
                    count += 1
                    if count == 1:
                        result.append(n)
                    else:
                        current = n
        result.append(current)
        return result
        
# link to question, https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/