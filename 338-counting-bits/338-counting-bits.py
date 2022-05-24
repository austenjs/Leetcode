class Solution:
    def __init__(self):
        self.memo = {0 : 0, 1 : 1}

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(self.countBit(i))
        return ans
        
    def countBit(self, n):
        if n in self.memo:
            return self.memo[n]
        if n % 2 == 1:
            ans = self.countBit(n // 2) + 1
        else:
            ans = self.countBit(n // 2)
        self.memo[n] = ans
        return ans