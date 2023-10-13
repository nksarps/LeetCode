class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        char_index = {}
        max_length = 0
        start = 0 
        for end in range(n):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end 
            max_length = max(max_length, end - start + 1)
        return max_length

# link to question, https://leetcode.com/problems/longest-substring-without-repeating-characters/