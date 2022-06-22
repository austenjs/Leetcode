class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        
        def backtrack(start = 0, cur = []):
            if sum(cur) == target:
                output.append(cur.copy())
                return
            elif sum(cur) > target:
                return
            seen = set()
            for i in range(start, N):
                num = candidates[i]
                if num in seen:
                    continue
                cur.append(num)
                backtrack(i + 1, cur)
                cur.pop()
                seen.add(num)
        
        output = []
        backtrack()
        return output