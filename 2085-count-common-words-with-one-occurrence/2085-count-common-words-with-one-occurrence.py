from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        ans = 0
        for word, count in counter1.items():
            if word not in words2:
                continue
            if count != 1:
                continue
            if counter2[word] != 1:
                continue
            ans += 1
        return ans