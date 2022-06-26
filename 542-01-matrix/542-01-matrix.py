import math

class Solution:
    def __init__(self):
        self.moves = [(0,  1),
                      (0, -1),
                      (1, 0),
                      (-1, 0)]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        ans = [[math.inf for _ in range(N)] for _ in range(M)]
        
        last_seen = None
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    ans[i][j] = 0
        
        # Top left
        for i in range(M):
            for j in range(N):
                if ans[i][j] == 0:
                    continue
                if i != 0 and j != 0:
                    ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1, ans[i][j - 1] + 1)
                elif i != 0:
                    ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1)
                elif j != 0:
                    ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1)
        
        # Bottom right
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if ans[i][j] == 0:
                    continue
                if i != M - 1 and j != N - 1:
                    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1, ans[i][j + 1] + 1)
                elif i != M - 1:
                    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1)
                elif j != N - 1:
                    ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1)
        
        return ans
