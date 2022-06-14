class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos = 0
        
        for i, num in enumerate(nums):
            if num % 2 == 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums