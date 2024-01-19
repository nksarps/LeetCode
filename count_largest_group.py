class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        count_dict = {}

        for i in range(1, n + 1):
            digit_sum_value = digit_sum(i)
            count_dict[digit_sum_value] = count_dict.get(digit_sum_value, 0) + 1

        max_count = max(count_dict.values())
        result = sum(1 for count in count_dict.values() if count == max_count)
        return result

# link to question, https://leetcode.com/problems/count-largest-group/