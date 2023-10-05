class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word[::-1] == word:
                return word
                exit()
        return ''
        
# link to question, https://leetcode.com/problems/find-first-palindromic-string-in-the-array/