class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums)
        num_to_index = {}
        for i, num in enumerate(sorted_array):
            if num not in num_to_index:
                num_to_index[num] = i
        return list(map(lambda num: num_to_index[num], nums))
        