class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        current = 0
        for num in nums:
            current += num
            if current > ans:
                ans = current
            if current < 0:
                current = 0
        return ans