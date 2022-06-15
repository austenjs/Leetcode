class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            addition = x ^ y
            carry = (x & y) << 1
            x, y = addition, carry
        
        return bin(x)[2:]