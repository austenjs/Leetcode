class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]
        for num in nums:
            counter[num] += 1
        index = 0
        while counter[0] > 0:
            nums[index] = 0
            index += 1
            counter[0] -= 1
        while counter[1] > 0:
            nums[index] = 1
            index += 1
            counter[1] -= 1
        while counter[2] > 0:
            nums[index] = 2
            index += 1
            counter[2] -= 1