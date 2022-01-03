class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}
        for i, num in enumerate(nums):
            number_to_index[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in number_to_index:
                complement_index = number_to_index[complement]
                if complement_index != i:
                    return [i, complement_index]
        return [-1, -1]