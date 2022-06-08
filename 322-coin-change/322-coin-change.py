class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1, 2, 5]
        # amt = 6
        # F(5) = 1
        # min(F(5 - 1), F(5 - 2), F(5 - 5)) + 1
        # F = [0, 1, 1, 2, 2, 1, 2]
        memo = [1e5 for _ in range(amount + 1)]
        memo[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i], memo[i - coin] + 1)
        
        return memo[amount] if memo[amount] != 1e5 else -1
        