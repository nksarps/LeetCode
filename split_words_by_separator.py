class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            parts = word.split(separator)
            result.extend(part for part in parts if part != '')
        return result

# link to question, https://leetcode.com/problems/split-strings-by-separator/submissions/