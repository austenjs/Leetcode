class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0:
                    ans = max(ans, self.floodFill(grid, i, j, M, N))
    
        return ans
        
    def floodFill(self, grid, i, j, M, N):
        if i < 0 or i == M or j < 0 or j == N:
            return 0
        if grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        ans = 1
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in moves:
            ans += self.floodFill(grid, i + x, j + y, M, N)
        return ans