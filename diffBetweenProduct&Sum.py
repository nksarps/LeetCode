class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1

        while n > 0:
            last_number = n % 10
            sum += last_number
            prod *= last_number
            n //= 10
        
        return prod - sum

# link, https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/