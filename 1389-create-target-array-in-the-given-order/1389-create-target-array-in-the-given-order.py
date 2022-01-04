class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new_array = []
        for i in range(len(nums)):
            new_array.insert(index[i], nums[i])
        return new_array