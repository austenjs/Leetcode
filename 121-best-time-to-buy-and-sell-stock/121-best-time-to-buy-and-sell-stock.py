import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur_min = math.inf
        for price in prices:
            if price < cur_min:
                cur_min = price
            ans = max(price - cur_min, ans)
        return ans