class Solution:
    def __init__(self):
        self.memo = {1 : 1, 2 : 2, 3 : 3}
        
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = ans
        return ans