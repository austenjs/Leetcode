from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S, P = len(s), len(p)
        counter = Counter(s[:P])
        counter_p = Counter(p)
        ans = []
        for i in range(S - P + 1):
            if counter == counter_p:
                ans.append(i)
            if i + P == S:
                break
            counter[s[i]] -= 1
            counter[s[i + P]] += 1
        return ans