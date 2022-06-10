import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        if N == k:
            return points
        
        dist_pivot = self.distance(points[random.randint(0, len(points) - 1)])
        left = []
        right = []
        for point in points:
            if self.distance(point) <= dist_pivot:
                left.append(point)
            else:
                right.append(point)
        
        if len(left) == k:
            return left
        elif len(left) < k:
            return left + self.kClosest(right, k - len(left))
        else:
            return self.kClosest(left, k)
            
    def distance(self, point):
        return point[0] * point[0] + point[1] * point[1]