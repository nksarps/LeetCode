class Solution:
    def fib(self, n: int) -> int:
        first_term  = 0
        second_term = 1
        new_term = 0
        if n == 0 or n == 1:
            return n
        else:
            for i in range(2, n + 1):
                new_term = first_term + second_term
                first_term = second_term
                second_term = new_term
            return new_term
