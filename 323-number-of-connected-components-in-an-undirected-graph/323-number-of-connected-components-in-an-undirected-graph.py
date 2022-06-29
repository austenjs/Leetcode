from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        def bfs(start):
            if start in visited:
                return 0
            queue = deque([start])
            while queue:
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for neighbor in adj_list[cur]:
                    queue.append(neighbor)
            return 1
        
        count = 0
        for i in range(n):
            count += bfs(i)
        return count
        
                