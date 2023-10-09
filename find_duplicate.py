class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        # Phase 1: Find the intersection point of the two pointers
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break  
        # Phase 2: Find the entrance of the cycle (the duplicate number)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

# link to question, https://leetcode.com/problems/find-the-duplicate-number/