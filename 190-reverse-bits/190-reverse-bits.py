class Solution:
    def reverseBits(self, n: int) -> int:
        string = bin(n)[2:]
        to_pad = 32 - len(string)
        return int(string[::-1] + '0' * to_pad, 2)