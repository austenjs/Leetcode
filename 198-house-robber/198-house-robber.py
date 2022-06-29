class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        dp = [0 for i in range(N)]
        
        for i in range(N):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[N - 1]