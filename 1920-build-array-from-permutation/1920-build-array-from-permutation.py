class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_array = []
        for num in nums:
            new_array.append(nums[num])
        return new_array