class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        
        arr.sort(key=lambda x: (count_ones(x), x))
        
        return arr


# link to question, https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/