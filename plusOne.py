class Solution:
    def plusOne(self, digit):
        n = len(digits) - 1
        i = 0
        new_digit = 0
        while n >= 0:
            new_digit += (10 ** n) * digits[i]
            print(new_digit)
            n -= 1
            i += 1
        new_digit += 1

        new_digit = str(new_digit)
        digits = list(new_digit)
        new_digits = []
        for digit in digits:
            digit = int(digit)
            new_digits.append(digit)
        return new_digits