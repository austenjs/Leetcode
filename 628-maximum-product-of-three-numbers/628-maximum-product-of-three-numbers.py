class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Base case
        if len(nums) < 3:
            return -1e10
        elif len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        
        nums = sorted(nums)
        # All positive
        if nums[0] >= 0:
            return nums[-1] * nums[-2] * nums[-3]
        # All negative
        if nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]
        
        return max(
            nums[0] * nums[1] * nums[2],
            nums[-3] * nums[-2] * nums[-1],
            nums[0] * nums[1] * nums[-1],
            nums[0] * nums[-2] * nums[-1]
        )