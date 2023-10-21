class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        count = 1
        while True:
            num = n * count
            if num % 2 == 0 and num % n == 0:
                return num
            count += 1 
        
# link to question, https://leetcode.com/problems/smallest-even-multiple/submissions/