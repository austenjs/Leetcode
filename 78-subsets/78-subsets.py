class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                output.append(curr.copy())
                return
            for i in range(first, N):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
                
        output = []
        N = len(nums)
        for k in range(N + 1):
            backtrack()
            
        return output