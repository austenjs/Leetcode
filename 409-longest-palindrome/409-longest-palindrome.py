from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        has_odd = False
        ans = 0
        count = Counter(s)
        for val in count.values():
            if val % 2:
                has_odd = True
                ans += val - 1
            else:
                ans += val
        return ans + has_odd