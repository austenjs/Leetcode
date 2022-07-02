class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        if N == 1:
            return min(costs[0])
        
        dp = [[0 for _ in range(3)] for _ in range(N)]
        
        dp[0] = costs[0]
        
        for i in range(1, N):
            # Pick R
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            # Pick B
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            # Pick G
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        return min(dp[-1])