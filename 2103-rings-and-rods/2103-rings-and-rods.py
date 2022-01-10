class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for color, index in zip(rings[0::2], rings[1::2]):
            rods[int(index)].add(color)
        ans = 0
        for rod in rods:
            ans += (len(rod) == 3)
        return ans
            