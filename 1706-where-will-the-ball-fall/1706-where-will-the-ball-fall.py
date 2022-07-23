class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        ans = []
        
        for i in range(N):
            x, y = 0, i
            output = -1
            while x < M and y >= 0 and y < N:
                direction = grid[x][y]
                if direction == 1: # right
                    if y == N - 1 or grid[x][y + 1] == -1:
                        break
                    y += 1
                elif direction == -1: # Left
                    if y == 0 or grid[x][y - 1] == 1:
                        break
                    y -= 1
                x += 1                
                
            # Ball Fall Succesfully
            if x == M and y >= 0 and y < N:
                output = y
            ans.append(output)
        return ans