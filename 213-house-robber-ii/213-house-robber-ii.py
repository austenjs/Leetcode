class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ignore_last = self.rob_linear(nums[:-1])
        ignore_first = self.rob_linear(nums[1:])
        return max(ignore_last, ignore_first)
    
    def rob_linear(self, nums):
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        
        prev_prev = prev = 0
        for i in range(N):
            cur = max(prev, prev_prev + nums[i])
            prev_prev, prev = prev, cur
        return cur