class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Using sum formula
        return N * (N + 1) // 2 - sum(nums)