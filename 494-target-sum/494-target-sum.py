class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited = {}
        def backtrack(idx = 0, total = 0):
            if idx == N:
                return 1 if total == target else 0
            if (idx, total) in visited:
                return visited[(idx, total)]
            ans = 0
            new_total = total + nums[idx]
            ans += backtrack(idx + 1, new_total)
            new_total = total - nums[idx]
            ans += backtrack(idx + 1, new_total)
            visited[(idx, total)] = ans
            return ans
        N = len(nums)
        ans = backtrack()
        return ans