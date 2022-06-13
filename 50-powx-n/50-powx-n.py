class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        
        square = self.myPow(x, int(n / 2))
        if n % 2:
            return square * square * x
        else:
            return square * square