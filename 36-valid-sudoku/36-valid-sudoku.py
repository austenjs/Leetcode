class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        M, N = len(board), len(board[0])
        for r in range(M):
            if self.valid_row(board, r, N):
                continue
            return False
        
        for c in range(N):
            if self.valid_col(board, c, M):
                continue
            return False
        
        r, R = 0, 3
        for _ in range(3):
            c, C = 0, 3
            for _ in range(3):
                if not self.valid_sub_box(board, r, R, c, C):
                    return False
                c, C = C, C + 3
            r, R = R, R + 3
        
        return True

    def valid_row(self, board, target_row, num_of_cols):
        seen = set()
        for c in range(num_of_cols):
            item = board[target_row][c]
            if item == '.':
                continue
            if item in seen:
                return False
            seen.add(item)
        return True
    
    def valid_col(self, board, target_col, num_of_rows):
        seen = set()
        for r in range(num_of_rows):
            item = board[r][target_col]
            if item == '.':
                continue
            if item in seen:
                return False
            seen.add(item)
        return True

    def valid_sub_box(self, board, r, R, c, C):
        seen = set()
        for i in range(r, R):
            for j in range(c, C):
                item = board[i][j]
                if item == '.':
                    continue
                if item in seen:
                    return False
                seen.add(item)
        return True