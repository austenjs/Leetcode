class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low_value = 9999
        profit = 0
        for i, num in enumerate(prices):
            if num < low_value:
                low_value = num
            new_profit = num - low_value
            if new_profit > profit:
                profit = new_profit
        return profit