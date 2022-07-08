import math

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = {}
        dp[(0, 0)] = triangle[0][0]
        for i in range(1, N):
            for j in range(i + 1):
                left = (i - 1, j - 1)
                right = (i - 1, j)
                left_val = math.inf
                right_val = math.inf
                if left in dp:
                    left_val = dp[left]
                if right in dp:
                    right_val = dp[right]
                dp[(i, j)] = min(left_val, right_val) + triangle[i][j]

        ans = math.inf
        for j in range(N):
            ans = min(ans, dp[(N - 1, j)])
        return ans
        