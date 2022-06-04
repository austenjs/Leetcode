class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        first_row = False
        first_col = False
        
        for i in range(num_rows):
            if matrix[i][0] == 0:
                first_col = True
        
        for j in range(num_cols):
            if matrix[0][j] == 0:
                first_row = True
        
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_col:
            for i in range(num_rows):
                matrix[i][0] = 0
            
        if first_row:
            for j in range(num_cols):
                matrix[0][j] = 0