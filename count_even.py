class Solution:
    def countEven(self, num: int) -> int:
        sum, result = 0, 0
        for i in range(1, num+1):
            while i != 0:
                n = i % 10
                sum += n
                i //= 10
            if sum % 2  == 0:
                result += 1
            sum = 0
        return result


#link: https://leetcode.com/problems/count-integers-with-even-digit-sum/