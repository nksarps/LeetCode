class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        first = 0
        last = 0
        for i in range(1, n + 1):
            if i % m != 0:
                first += i
            else:
                last += i
        return first - last

# link, https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/