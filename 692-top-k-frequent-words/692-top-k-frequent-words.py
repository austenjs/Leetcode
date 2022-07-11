from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        N = len(words)
        n_largest = heapq.nlargest(N,
                                   [(word, count) for word, count in counter.items()],
                                   key = lambda x : (-x[1], x[0]))
        print(n_largest)
        ans = [item for item in n_largest[-k:]]
        return [item[0] for item in reversed(ans)]