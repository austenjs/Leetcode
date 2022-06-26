class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        num_of_islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '0':
                    continue
                self.floodfill(grid, i, j, M, N)
                num_of_islands += 1
        return num_of_islands
    
    def floodfill(self, grid, i, j, M, N):
        if i < 0 or i == M or j < 0 or j == N:
            return
        if grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in moves:
            self.floodfill(grid, i + x, j + y, M, N)