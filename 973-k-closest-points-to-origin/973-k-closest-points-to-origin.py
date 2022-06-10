class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        if N == k:
            return points
        sorted_points = sorted(points, key = lambda x : x[0] * x[0] + x[1] * x[1])
        return sorted_points[:k]