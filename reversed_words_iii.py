class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        reversed_sentence = ' '.join(reversed_words)
        return reversed_sentence

# link to question, https://leetcode.com/problems/reverse-words-in-a-string-iii/