class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].     islower()):
            return True
        return False

# link to question, https://leetcode.com/problems/detect-capital/submissions/