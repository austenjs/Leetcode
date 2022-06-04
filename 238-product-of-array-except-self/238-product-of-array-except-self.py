class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0 for _ in range(N)]
        
        ans[0] = 1
        for i in range(1, N):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        R = 1
        for i in reversed(range(N)):
            ans[i] = ans[i] * R
            R *= nums[i]
        
        return ans