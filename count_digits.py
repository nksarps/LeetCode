class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        count = 0
        for n in str_num:
            if num % int(n) == 0:
                count += 1
        return count
        
# link to question, https://leetcode.com/problems/count-the-digits-that-divide-a-number/