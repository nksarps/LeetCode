class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        pascals_triangle = []

        for i in range(numRows):
            if i == 0:
                pascals_triangle.append([1])
            else:
                prev_row = pascals_triangle[i - 1]
                current_row = [1]  # The first element of each row is always 1
                for j in range(1, i):
                    current_row.append(prev_row[j - 1] + prev_row[j])
                current_row.append(1)  # The last element of each row is always 1
                pascals_triangle.append(current_row)

        return pascals_triangle

# link to question, https://leetcode.com/problems/pascals-triangle/