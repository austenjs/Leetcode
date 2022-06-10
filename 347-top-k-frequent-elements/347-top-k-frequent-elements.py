from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        tmp = [(key, val) for key, val in num_count.items()]
        return list(map(lambda x : x[0], heapq.nlargest(k, tmp, key = lambda x: x[1])))