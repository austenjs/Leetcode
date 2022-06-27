from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        start_node = None
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '*':
                    start_node = (i, j, 0) # x, y, dist
                    break
        
        queue = deque()
        queue.append(start_node)
        visited = set()
        
        while queue:
            x, y, dist = queue.popleft()
            if (x, y) in visited:
                continue
            if x < 0 or x == M or y < 0 or y == N:
                continue
            if grid[x][y] == '#':
                return dist
            elif grid[x][y] == 'X':
                continue
            visited.add((x, y))
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for ix, iy in moves:
                queue.append((x + ix, y + iy, dist + 1))
        
        return -1
                