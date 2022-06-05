class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        index = 0
        count = 0
        
        for num in nums:
            if num == 0:
                count += 1
        
        while index < N and count:
            if nums[index] == 0:
                nums.append(nums.pop(index))
                count -= 1
            else:
                index += 1

            