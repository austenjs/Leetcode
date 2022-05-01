class Solution:
    def canWinNim(self, n: int) -> bool:
        return n <= 3 or n % 4