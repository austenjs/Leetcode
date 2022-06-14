class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return '0'
        if n == 2:
            return '01'[k - 1]
        mid = 2 ** (n - 2)
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        offset = 0 if k < 3 else 2 ** (n - 3)   
        if k <= 3 / 2 * mid:
            return self.kthGrammar(n - 1, k - mid + offset)
        else:
            return self.kthGrammar(n - 1, k - mid - offset)