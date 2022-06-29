from collections import deque, defaultdict
class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, child):
        if child != self.parents[child]:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]

class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for child, parent in edges:
            uf.union(child, parent)
        
        parents = set()
        for i in range(n):
            parents.add(uf.find(i))
        return len(parents)
        
                