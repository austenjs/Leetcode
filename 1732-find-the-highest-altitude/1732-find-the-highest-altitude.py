class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_height = 0
        for g in gain:
            current += g
            max_height = max(current, max_height)
        return max_height