import itertools
indices = list(itertools.permutations([0, 1, 2, 3]))

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        ans = 9999
        for i, j, k, l in indices:
            candidate = digits[i] * 10 + digits[j] + digits[k] * 10 + digits[l]
            ans = min(ans, candidate)
        return ans
