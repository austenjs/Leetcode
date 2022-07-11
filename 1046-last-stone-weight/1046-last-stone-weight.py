import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        N = len(stones)
        for i in range(N):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, x - y)
        return -heapq.heappop(stones) if stones else 0