class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)
        nums = sorted(nums)
        min_allowed = nums[0]
        ans = 0
        for num in nums:
            if num < min_allowed:
                ans += min_allowed - num
                num = min_allowed
            min_allowed = num + 1
        return ans