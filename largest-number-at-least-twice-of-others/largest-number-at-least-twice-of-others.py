class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxim = max_index = -1
        for i, num in enumerate(nums):
            if num > maxim:
                maxim = num
                max_index = i
        for num in nums:
            if num != maxim and num * 2 > maxim:
                return -1
        return max_index