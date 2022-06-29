class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        prev_prev = prev = 0
        
        for i in range(N):
            cur = max(prev, prev_prev + nums[i])
            prev_prev, prev = prev, cur
        return cur