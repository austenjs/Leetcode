class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)
        if size != m * n:
            return []
        
        ans = []
        tmp = []
        for i, num in enumerate(original):
            if i != 0 and i % n == 0:
                ans.append(tmp)
                tmp = []
            tmp.append(num)
        
        ans.append(tmp)
        return ans