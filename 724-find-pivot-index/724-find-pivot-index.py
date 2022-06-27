class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        idx = 0
        N = len(nums)
        while idx < N:
            if idx != 0:
                left += nums[idx - 1]
            right -= nums[idx]
            if left == right:
                return idx
            idx += 1
        return -1