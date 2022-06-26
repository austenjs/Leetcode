class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        def backtrack(start = 0, cur = []):
            if sum(cur) == target:
                output.append(cur.copy())
                return
            elif sum(cur) > target:
                return
            else:
                for i in range(start, N):
                    cur.append(candidates[i])
                    backtrack(i, cur)
                    cur.pop()
        
        output = []
        backtrack()
        return output