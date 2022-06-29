class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        if target in nums:
            return True
    
        N = len(nums)
        dp = [[False for _ in range(total + 1)] for _ in range(N + 1)]
        dp[0][0] = True
        for i in range(1, N + 1):
            cur = nums[i - 1]
            for j in range(target + 1):
                if j < cur:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - cur] or dp[i - 1][j]
        return dp[N][target]
        
        