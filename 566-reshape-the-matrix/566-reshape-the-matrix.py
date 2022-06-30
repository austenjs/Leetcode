class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:        
        M, N = len(mat), len(mat[0])
        if M * N != r * c:
            return mat
        
        new_ans = [[0 for _ in range(c)] for _ in range(r)]
        p_r = p_c = 0
        
        for i in range(M):
            for j in range(N):
                new_ans[p_r][p_c] = mat[i][j]
                p_c += 1
                if p_c == c:
                    p_r += 1
                    p_c = 0
        return new_ans