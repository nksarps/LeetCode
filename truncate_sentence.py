class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        n = 0
        arr_s = []
        return_str = ''
        while n < k:
            if not n == k - 1:
                return_str += s[n]
                return_str += ' '
            else:
                return_str += s[n]
            n += 1
        return return_str

# link to question, https://leetcode.com/problems/truncate-sentence/