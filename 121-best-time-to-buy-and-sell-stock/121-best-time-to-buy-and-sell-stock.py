class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        N = len(prices)
        ans = 0
        
        while right < N:
            if prices[right] < prices[left]:
                left = right
            else:
                ans = max(ans, prices[right] - prices[left])
            right += 1
        
        return ans