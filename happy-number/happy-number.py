class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sum_digits = 0
            while n:
                sum_digits += (n % 10) ** 2
                n //= 10
            n = sum_digits
        return True