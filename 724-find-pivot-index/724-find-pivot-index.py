class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == S - leftsum - num:
                return i
            leftsum += num
        return -1