class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.M = len(board)
        self.N = len(board[0])
        self.board = board
        
        for i in range(self.M):
            for j in range(self.N):
                if self.backtrack(i, j, word):
                    return True
        
        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True
        if row < 0 or col < 0 or row >= self.M or col >= self.N or self.board[row][col] != suffix[0]:
            return False
        
        ret = False
        
        self.board[row][col] = '#'
        for incRow, incCol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ret = self.backtrack(row + incRow, col + incCol, suffix[1:])
            if ret:
                break
        
        self.board[row][col] = suffix[0]
        
        return ret