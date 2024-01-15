from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1_obj = datetime.strptime(date1, '%Y-%m-%d')
        date2_obj = datetime.strptime(date2, '%Y-%m-%d')

        delta = abs(date2_obj - date1_obj)
        
        return delta.days

# link to question, https://leetcode.com/problems/number-of-days-between-two-dates/