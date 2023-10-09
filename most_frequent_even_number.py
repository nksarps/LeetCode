class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_count = 0
        result = float('inf')  # Initialize result to positive infinity #2404
        for num in nums:
            if num % 2 == 0:
                count = nums.count(num)
                if count > even_count or (count == even_count and num < result):
                    even_count = count
                    result = num
        if even_count == 0:
            return -1
        return result

# link to question, https://leetcode.com/problems/most-frequent-even-element/