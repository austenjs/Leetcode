from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = Counter(s)
        sorted_freq = sorted([freq for freq in frequencies.values()])
        ans = 0
        seen = set()
        for freq in sorted_freq:
            if freq not in seen:
                pass
            else:
                while freq:
                    print(freq, seen)
                    if freq not in seen:
                        break
                    freq -= 1
                    ans += 1
            seen.add(freq)
        return ans