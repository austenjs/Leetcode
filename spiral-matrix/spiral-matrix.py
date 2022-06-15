class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        visited = set()
        i = j = 0
        
        going_right = True
        going_down = False
        going_left = False
        going_up = False

        while True:
            if (i, j) in visited or i < 0 or j < 0 or i == num_rows or j == num_cols:
                break
            ans.append(matrix[i][j])
            visited.add((i, j))
            if going_up:
                if  i - 1 < 0 or (i - 1, j) in visited:
                    going_right = True
                    going_up = False
                    j = j + 1
                else:
                    i = i - 1
            elif going_down:
                if i + 1 == num_rows or (i + 1, j) in visited:
                    going_left = True
                    going_down = False
                    j = j - 1
                else:
                    i = i + 1
            elif going_left:
                if j - 1 < 0 or (i , j - 1) in visited:
                    going_up = True
                    going_left = False
                    i = i - 1
                else:
                    j = j - 1
            elif going_right:
                if j + 1 == num_cols or (i, j + 1) in visited:
                    going_down = True
                    going_right = False
                    i = i + 1
                else:
                    j = j + 1
        return ans
            