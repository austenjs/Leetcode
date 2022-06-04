class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        rows = [False for _ in range(num_rows)]
        cols = [False for _ in range(num_cols)]
        
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(num_rows):
            for j in range(num_cols):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0