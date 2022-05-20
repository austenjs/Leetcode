class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR and count bit = 1
        return bin(start ^ goal).count("1")