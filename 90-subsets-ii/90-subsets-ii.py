class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(first = 0, cur = []):
            if len(cur) == k:
                output.append(cur.copy())
                return
            seen = set()
            for i in range(first, N):
                num = nums[i]
                if num in seen:
                    continue
                cur.append(num)
                backtrack(i + 1, cur)
                cur.pop()
                seen.add(num)
        
        output = []
        N = len(nums)
        for k in range(N + 1):
            backtrack()
        return output