class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        palindrome_length = 0
        odd_char_count = 0
        for count in char_count.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                odd_char_count = 1
        if odd_char_count:
            palindrome_length += 1 
        return palindrome_length

# link to question, https://leetcode.com/problems/longest-palindrome/