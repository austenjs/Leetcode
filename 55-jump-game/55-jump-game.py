class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_of_jump = nums[0]
        idx = 0
        N = len(nums)
        if N == 1:
            return True
        while num_of_jump and idx < N:
            num_of_jump = max(num_of_jump - 1, nums[idx])
            idx += 1  
        return idx == N