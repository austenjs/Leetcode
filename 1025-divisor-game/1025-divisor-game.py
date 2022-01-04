memo = {1 : False, 2 : True, 3 : False}

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n in memo:
            return memo[n]
        last = 1
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                last = i
                if i in memo and memo[i]:
                    memo[n] = True
                    return True
        return not self.divisorGame(n - last)