class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        result = 0
        for word in words1:
            if word in words2:
                if words1.count(word) == 1 and words2.count(word) == 1:
                    result += 1
        return result 
        
# link to question, https://leetcode.com/problems/count-common-words-with-one-occurrence/