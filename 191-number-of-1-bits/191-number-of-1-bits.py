class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        mask = 1
        for i in range(32):
            if (n & mask):
                ans += 1
            mask = mask << 1
        return ans