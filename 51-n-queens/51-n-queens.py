class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = set()
        board = [[False for _ in range(n)] for _ in range(n)]
        
        def backtrack(row = 0, ans = []):
            for col in range(n):
                if not under_attack(row, col):
                    board[row][col] = True
                    queens.add((row, col))
                    if row == n - 1:
                        ans.append(generate_board())
                    else:
                        ans = backtrack(row + 1, ans)
                    queens.remove((row, col))
                    board[row][col] = False
            return ans
    
        def under_attack(row, col):
            for queen in queens:
                q_row, q_col = queen
                # Horizontal or vertical
                if row == q_row or col == q_col:
                    return True
                # Diagonal
                if (row - q_row == col - q_col) or (row - q_row + col - q_col == 0):
                    return True
            return False
            
        def generate_board():
            ans = []
            for row in board:
                cur = ''
                for item in row:
                    if item:
                        cur += 'Q'
                    else:
                        cur += '.'
                ans.append(cur)
            return ans
        
        return backtrack()