from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for edge in edges:
            count[edge[0]] += 1
            count[edge[1]] += 1
        N = len(edges)
        for key, val in count.items():
            if val == N:
                return key
        return -1