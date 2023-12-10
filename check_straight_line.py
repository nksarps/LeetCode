class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True  
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        initial_slope = float('inf') if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)

        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]
            current_slope = float('inf') if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)

            if current_slope != initial_slope:
                return False
        return True

# link to question, https://leetcode.com/problems/check-if-it-is-a-straight-line/