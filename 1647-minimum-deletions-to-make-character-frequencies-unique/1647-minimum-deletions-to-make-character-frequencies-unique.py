from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = Counter(s)
        sorted_freq = sorted([freq for freq in frequencies.values()], reverse = True)

        ans = 0
        max_allowed = len(s)
        for freq in sorted_freq:
            if freq > max_allowed:
                ans += freq - max_allowed
                freq = max_allowed
            max_allowed = max(0, freq - 1)
        return ans