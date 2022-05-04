from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter1 = Counter(s1.split())
        counter2 = Counter(s2.split())
        set1 = set()
        set2 = set()
        for word, count in counter1.items():
            if count > 1 or word in counter2:
                continue
            set1.add(word)
        for word, count in counter2.items():
            if count > 1 or word in counter1:
                continue
            set2.add(word)
        return list(set1 ^ set2)