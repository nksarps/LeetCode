class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index = word.index(ch)
        reversed_part = word[:index + 1][::-1]
        result = reversed_part + word[index + 1:]
        return result

# link to question, https://leetcode.com/problems/reverse-prefix-of-word/