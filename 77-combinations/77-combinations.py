class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(start = 1, cur = []):
            if len(cur) == k:
                output.append(cur.copy())
                return
            for i in range(start, n + 1):
                cur.append(i)
                backtrack(i + 1, cur)
                cur.pop()
        backtrack()
        return output