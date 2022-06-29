class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        area = 0
        left, right = 0, N - 1
        while left <= right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area