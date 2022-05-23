class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10000
        current = 0
        for num in nums:
            current += num
            ans = max(ans, current)
            current = 0 if current < 0 else current
        return ans