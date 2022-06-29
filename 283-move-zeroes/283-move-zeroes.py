class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        N = len(nums)
        for i in range(N):
            num = nums[i]
            if num != 0:
                nums[left], nums[i] = num, nums[left]
                left += 1
