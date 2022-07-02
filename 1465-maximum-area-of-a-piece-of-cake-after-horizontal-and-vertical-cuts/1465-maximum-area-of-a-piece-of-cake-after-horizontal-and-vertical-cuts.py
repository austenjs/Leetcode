class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        prev = 0
        max_h = 0
        
        horizontalCuts.sort()
        for h_cut in horizontalCuts:
            max_h = max(max_h, h_cut - prev)
            prev = h_cut
        max_h = max(max_h, h - prev)
        
        prev = 0
        max_c = 0
        verticalCuts.sort()
        for c_cut in verticalCuts:
            max_c = max(max_c, c_cut - prev)
            prev = c_cut
        max_c = max(max_c, w - prev)
        
        return max_h * max_c % (10**9 + 7)