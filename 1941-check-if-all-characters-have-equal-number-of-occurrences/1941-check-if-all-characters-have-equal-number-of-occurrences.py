from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        previous = -1
        for key in count.keys():
            if previous == -1:
                previous = count[key]
            elif previous != count[key]:
                return False
        return True