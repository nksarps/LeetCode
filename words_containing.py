class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        start = 0
        for word in words:
            if x in word:
                result.append(start)
            start += 1
        return result

# link to question, https://leetcode.com/problems/find-words-containing-character/