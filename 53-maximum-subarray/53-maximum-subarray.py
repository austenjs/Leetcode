class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            current_sum = max(current_sum, 0)
            ans = max(ans, current_sum)
        return ans if ans > 0 else max(nums)