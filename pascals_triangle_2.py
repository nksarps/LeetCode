class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        current_row = [1]

        for i in range(1, rowIndex + 1):
            next_row = [1]  # The first element of each row is always 1
            for j in range(1, len(current_row)):
                next_row.append(current_row[j - 1] + current_row[j])
            next_row.append(1)  # The last element of each row is always 1
            current_row = next_row

        return current_row

# link to question, https://leetcode.com/problems/pascals-triangle-ii/