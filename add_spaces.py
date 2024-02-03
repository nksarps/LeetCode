class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = [i for i in re.split("([A-Z][^A-Z]*)", s) if i] # spliting string wherever there's a capital letter
        result = ''
        counter = 0
        while counter < len(s):
            result += s[counter]
            result += ' '
            counter += 1
        return result.strip()

#🚧  link, https://leetcode.com/problems/adding-spaces-to-a-string/