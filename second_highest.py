class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = []
        for ch in s:
            if ch.isnumeric():
                numbers.append(int(ch))
        if len(numbers) != 0:
            max_num = max(numbers)
            sec_max = 0
            for num in numbers:
                if num != max_num:
                    if num > sec_max:
                        sec_max = num
            if sec_max == 0:
                return -1
            return sec_max
        return -1

# link, https://leetcode.com/problems/second-largest-digit-in-a-string/