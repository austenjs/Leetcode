class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        ans = 0
        for i in range(1, N):
            point1, point2 = points[i-1], points[i]
            diff_x = abs(point1[0] - point2[0])
            diff_y = abs(point1[1] - point2[1])
            ans += max(diff_x, diff_y)
        return ans