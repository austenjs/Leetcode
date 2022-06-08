class Solution:
    def __init__(self):
        self.memo = {0 : 0}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]

        # Base case
        if amount < min(coins):
            self.memo[amount] = -1
            return -1
        for coin in coins:
            if coin == amount:
                self.memo[coin] = 1
                return 1
        
        minimum = 10000
        for coin in reversed(sorted(coins)):
            additional_coins = self.coinChange(coins, amount - coin)
            if additional_coins == -1:
                continue
            minimum = min(minimum, additional_coins)
        
        ans = 0
        if minimum == 10000:
            ans = -1
        else:
            ans = 1 + minimum
        
        self.memo[amount] = ans
        return ans