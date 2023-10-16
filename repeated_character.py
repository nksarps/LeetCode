class Solution:
    def repeatedCharacter(self, s: str) -> str:
        arr = []
        for char in s:
            if char in arr:
                return char
            else:
                arr.append(char) 

# link to question, https://leetcode.com/problems/first-letter-to-appear-twice/