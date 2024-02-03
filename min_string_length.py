class Solution:
    def minimizedStringLength(self, s: str) -> int:
        result = ''
        counter = 0
        while counter < len(s):
            if s[counter] not in result:
                result += s[counter]
            counter += 1
        return len(result)
        
# link, https://leetcode.com/problems/minimize-string-length/