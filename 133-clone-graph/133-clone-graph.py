"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':  
        if node is None:
            return node
        
        nodes = [Node(i) for i in range(1, 101)]
        adj_list = self.create_adj_list(node)
        for key, neighbors in adj_list.items():
            for neighbor in neighbors:
                nodes[key - 1].neighbors.append(nodes[neighbor - 1])
                
        return nodes[node.val - 1]

    def create_adj_list(self, node):
        adj_list = defaultdict(set)
        visited = set()
        
        queue = deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in cur.neighbors:
                queue.append(neighbor)
                adj_list[cur.val].add(neighbor.val)
        
        return adj_list
        