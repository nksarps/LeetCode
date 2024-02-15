class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = [char for char in t]
        s = [char for char in s]
        
        for char in t:
            if s.count(char) < t.count(char):
                return char
            if not char in s:
                return char


# link, https://leetcode.com/problems/find-the-difference