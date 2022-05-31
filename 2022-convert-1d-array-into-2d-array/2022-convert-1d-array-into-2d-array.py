class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        ans = []
        index = 0
        for i in range(m):
            ans.append([])
            for _ in range(n):
                ans[i].append(original[index])
                index += 1
        
        return ans