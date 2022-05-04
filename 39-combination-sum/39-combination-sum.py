from collections import deque

class Node:
    def __init__(self, elements):
        self.total = sum(elements)
        self.elements = elements
    
    def insert(self, element):
        self.total += element
        self.elements.append(element)

class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        queue = deque()
        visited = set()
        ans = []
        inserted = set()
        
        start_node = Node([])
        queue.append(start_node)
        
        while queue:
            node = queue.popleft()
            if node.total > target or node in visited:
                continue
            if node.total == target:
                check = tuple(sorted(node.elements))
                if check in inserted:
                    continue
                ans.append(list(check))
                inserted.add(check)
                continue
            visited.add(node)
            total = node.total
            elements = node.elements.copy()
            for candidate in candidates:
                tmp = elements.copy()
                tmp.append(candidate)
                queue.append(Node(tmp))
        return ans