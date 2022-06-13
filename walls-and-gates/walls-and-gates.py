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
        
        for row, col in starts:
            self.bfs(rooms, row, col)
            
    def bfs(self, rooms, row, col):
        queue = deque()
        queue.extend([(row + 1, col, 1), (row - 1, col, 1), (row, col + 1, 1), (row, col - 1, 1)]) # i, j, distance
        visited = set()
        
        while len(queue):
            row, col, distance = queue.popleft()
            if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
                continue
            if rooms[row][col] <= 0:
                continue
            if (row, col) in visited:
                continue

            visited.add((row, col))
            if rooms[row][col] <= distance:
                continue
            rooms[row][col] = distance
            for incRow, incCol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                queue.append((row + incRow, col + incCol, distance + 1))
            