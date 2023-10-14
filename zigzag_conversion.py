class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s 
        rows = [''] * numRows
        current_row = 0
        moving_down = False
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                moving_down = not moving_down
            current_row += 1 if moving_down else -1
        result = ''.join(rows)
        return result

# link to question, https://leetcode.com/problems/zigzag-conversion/