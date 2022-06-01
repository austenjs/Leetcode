class Solution:
    def flood(self, image, sr, sc, target, newColor):
        if sr < 0 or sr >= len(image):
            return
        if sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != target or image[sr][sc] == newColor:
            return
        image[sr][sc] = newColor
        self.flood(image, sr + 1, sc, target, newColor)
        self.flood(image, sr - 1, sc, target, newColor)
        self.flood(image, sr, sc + 1, target, newColor)
        self.flood(image, sr, sc - 1, target, newColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.flood(image, sr, sc, image[sr][sc], newColor)
        return image