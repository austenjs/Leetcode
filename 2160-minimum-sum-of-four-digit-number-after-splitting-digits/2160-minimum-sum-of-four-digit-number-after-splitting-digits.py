class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits = sorted(digits)
        return digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3]
