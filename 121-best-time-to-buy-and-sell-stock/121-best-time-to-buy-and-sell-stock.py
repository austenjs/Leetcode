import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur_min = math.inf
        for price in prices:
            if price < cur_min:
                cur_min = price
            elif price - cur_min > ans:
                ans = price - cur_min
        return ans