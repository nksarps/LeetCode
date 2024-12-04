class Solution:
    def addToArrayForm(self, num, k):
        n = len(num)
        result = []
        carry = k
        
        for i in range(n - 1, -1, -1):
            curr_sum = num[i] + carry     
            result.append(curr_sum % 10)
            carry = curr_sum // 10
        
        while carry > 0:
            result.append(carry % 10)
            carry //= 10
        
        return result[::-1]

#link: https://leetcode.com/problems/add-to-array-form-of-integer/description/