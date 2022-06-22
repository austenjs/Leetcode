class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        def backtrack(start = 0, cur = []):
            if len(cur) == k:
                if sum(cur) == n:
                    output.append(cur.copy())
                return
            for i in range(start, 9):
                candidate = candidates[i]
                if candidate not in cur:
                    cur.append(candidate)
                    backtrack(i + 1, cur)
                    cur.pop()
            return
        
        output = []
        backtrack()
        return output