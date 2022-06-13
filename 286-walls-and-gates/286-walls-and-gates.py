from collections import deque

INF = 2147483647

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.ROWS = len(rooms)
        self.COLS = len(rooms[0])
        
        starts = []
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if rooms[i][j] == 0:
                    starts.append((i, j))
        if len(starts) == 0:
            return
        self.bfs(rooms, starts)
            
    def bfs(self, rooms, starts):
        queue = deque()
        queue.extend(starts)
        
        while len(queue):
            row, col = queue.popleft()
            for incRow, incCol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + incRow, col + incCol
                if new_row < 0 or new_row >= self.ROWS or new_col < 0 or new_col >= self.COLS or rooms[new_row][new_col] != INF:
                    continue
                rooms[new_row][new_col] = rooms[row][col] + 1
                queue.append((new_row, new_col))
            