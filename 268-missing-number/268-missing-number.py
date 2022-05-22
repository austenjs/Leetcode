class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)

        # O(1) seek
        num_in_nums = set(nums)
        
        for i in range(0, N + 1):
            if i not in num_in_nums:
                return i
        return -1