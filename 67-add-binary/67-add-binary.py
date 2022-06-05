class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            tmp = x ^ y
            carry = (x & y) << 1
            x, y = tmp, carry
        
        return bin(x)[2:]