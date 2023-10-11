class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = 0
        for num in arr:
            if arr.count(num) == num:
                if num > lucky:
                    lucky = num
        if lucky == 0:
            return -1
        return lucky 

# link to question, https://leetcode.com/problems/find-lucky-integer-in-an-array/