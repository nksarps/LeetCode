class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = [ch for ch in s]
        result = ''

        for ch in range(len(s)):
            if not ch in spaces:
                result += s[ch]
            else:
                result += ' '
                result += s[ch]
                
        return result

    # link , https://leetcode.com/problems/adding-spaces-to-a-string/