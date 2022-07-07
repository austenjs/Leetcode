class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        
        dp = [0 for _ in range(N + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, N + 1):
            if i == N:
                dp[i] = min(dp[i - 1], dp[i - 2])
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        return dp[N]