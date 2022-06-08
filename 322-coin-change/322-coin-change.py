class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [1e5 for _ in range(amount + 1)]
        memo[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i], memo[i - coin] + 1)
        
        return memo[amount] if memo[amount] != 1e5 else -1
        