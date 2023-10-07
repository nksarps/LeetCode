class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return_str = ''
        for word in words:
            char = word[0]
            return_str += char
        if return_str == s:
            return True
        return False
        
# link to question, https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/