memo = {0 : 0, 1 : 1, 2 : 1}

class Solution:
    def fib(self, n: int) -> int:
        if n in memo:
            return memo[n]
        ans = self.fib(n - 1) + self.fib(n - 2)
        memo[n] = ans
        return ans