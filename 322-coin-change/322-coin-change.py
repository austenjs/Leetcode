class Solution:
    def __init__(self):
        self.memo = {0 : 0}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        for coin in coins:
            self.memo[coin] = 1
        return self.getMinCoins(sorted(coins)[::-1], amount)

    def getMinCoins(self, coins, amount):
        # Base case
        if amount < 0:
            return -1
        if amount in self.memo:
            return self.memo[amount]
        
        minimum = 10000
        for coin in coins:
            additional_coins = self.getMinCoins(coins, amount - coin)
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