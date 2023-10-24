class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for word in sentence:
            if word.startswith(searchWord):
                return sentence.index(word) + 1
        return -1
        
# link to question, https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/