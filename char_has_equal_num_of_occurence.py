class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        checker = s.count(s[0])
        for char in s:
            if not s.count(char) == checker:
                return False
        return True 
        
# link to question, https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/