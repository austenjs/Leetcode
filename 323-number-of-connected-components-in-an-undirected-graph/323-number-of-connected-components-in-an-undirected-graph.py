from collections import deque, defaultdict
class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))
        self.ranks = [0 for _ in range(N)]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = self.parents[parent_x]
        elif self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = self.parents[parent_y]
        else:
            self.parents[parent_x] = self.parents[parent_y]
            self.ranks[parent_y] += 1

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
        
                