memo = {1 : 1, 2 : 2, 3 : 3}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in memo:
            return memo[n]
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        memo[n] = ans
        return ans