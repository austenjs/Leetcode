class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maximum = [0 for _ in range(N)]
        minimum = [1e4 for _ in range(N)]
        
        maximum[N - 1] = prices[N - 1]
        minimum[0] = prices[0]
        for i in range(N - 2, -1, -1):
            maximum[i] = max(maximum[i + 1], prices[i])
        
        for i in range(1, N):
            minimum[i] = min(minimum[i - 1], prices[i])
        
        ans = 0
        for i in range(N):
            ans = max(ans, maximum[i] - minimum[i])
        return ans