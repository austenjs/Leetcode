class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        current = 0
        for num in nums:
            current += num
            ans = current if current > ans else ans
            current = 0 if current < 0 else current
        return ans