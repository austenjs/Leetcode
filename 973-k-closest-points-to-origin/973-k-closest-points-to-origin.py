class Solution:
    def calculateDistance(self, point):
        return point[0] * point[0] + point[1] * point[1]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 1:
            return [min(points, key = lambda point : self.calculateDistance(point))]
        if len(points) == k:
            return points
        pivot_point = points[len(points) // 2]
        pivot = self.calculateDistance(pivot_point)
        left = []
        right = []
        for point in points:
            if point == pivot_point:
                continue
            if self.calculateDistance(point) > pivot:
                right.append(point)
            else:
                left.append(point)
        if len(left) == k:
            return left
        elif len(left) == k - 1:
            left.append(pivot_point)
            return left
        elif len(left) < k:
            left.append(pivot_point)
            return left + self.kClosest(right, k - len(left))
        else:
            return self.kClosest(left, k)