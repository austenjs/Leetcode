class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = set()
        
        def backtrack(row, count):
            for col in range(n):
                if not under_attack(row, col):
                    queens.add((row, col))
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    queens.remove((row, col))
            return count
        
        def under_attack(row, col):
            for queen in queens:
                q_row, q_col = queen
                # Vertical or Horizontal
                if q_row == row or q_col == col:
                    return True
                if (row - q_row == col - q_col) or (row - q_row + col - q_col == 0):
                    return True
            return False
        
        count = backtrack(0, 0)
        return count