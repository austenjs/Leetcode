from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1, count2 = Counter(s), Counter(t)
        return count1 == count2