class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, depth = 0):
            if depth == N:
                output.append(nums.copy())
                return
            for i in range(first, N):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1, depth + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        output = []
        N = len(nums)
        backtrack()
        return output