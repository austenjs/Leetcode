import math
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        exist_fresh = False
        dist_matrix = [[math.inf for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    dist_matrix[i][j] = 0
                exist_fresh = True
        if not exist_fresh:
            return 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 2:
                    continue
                self.flood_fill(grid, dist_matrix, i, j, M, N, 0)
        
        print(dist_matrix)
        max_dist = max(max(row) for row in dist_matrix)
        if max_dist == math.inf:
            return -1
        return max_dist
        
    def flood_fill(self, grid, distance_matrix, i, j, M, N, distance):
        if i < 0 or j < 0 or i == M or j == N:
            return
        if distance and grid[i][j] != 1:
            return
        if distance_matrix[i][j] <= distance:
            return

        distance_matrix[i][j] = distance
        moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        for x, y in moves:
            self.flood_fill(grid, distance_matrix, i + x, j + y, M, N, distance + 1)