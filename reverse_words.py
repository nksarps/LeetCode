class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split() if word]
        result = ' '.join(words[::-1])
        return result

# link to question, https://leetcode.com/problems/reverse-words-in-a-string/