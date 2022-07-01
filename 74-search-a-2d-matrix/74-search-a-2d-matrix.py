class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        left, right = 0, M * N - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // N
            col = mid % N
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False