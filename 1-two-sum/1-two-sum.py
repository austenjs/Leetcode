class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i
            
            
            
            
            
            \
            
            
        for i, num in enumerate(nums):
            
            complement = target - num
            if complement not in num_to_index:
                continue
            index = num_to_index[complement]
            if index == i:
                continue
            return [i, index]
        return [-1, -1]