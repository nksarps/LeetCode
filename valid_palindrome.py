class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr_s = []
        arr_s_reversed = []
        n = 0
        while n < len(s):
            if s[n].isalnum(): # check if number is an alpha-numeric
                arr_s.append(s[n])
            n += 1
        arr_s_reversed = arr_s[::-1] # arr_s[::-1] is reversing arr_s
        if arr_s == arr_s_reversed:
            return True
        return False
        

# link to question, https://leetcode.com/problems/valid-palindrome/