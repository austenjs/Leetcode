class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(self.countBit(i))
        return ans
        
    def countBit(self, n):
        ans = 0
        current = 1
        while 2 * current <= n:
            current *= 2
        while n > 0:
            if n >= current:
                n -= current
                ans += 1
            current //= 2
        return ans