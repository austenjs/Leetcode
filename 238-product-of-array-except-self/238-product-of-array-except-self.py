class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [0 for _ in range(N)]
        right = [0 for _ in range(N)]
        
        left[0] = nums[0]
        for i in range(1, N):
            left[i] = left[i - 1] * nums[i]
        
        right[-1] = nums[-1]
        for i in range(N - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]
            
        ans = []
        ans.append(right[1])
        
        for i in range(1, N - 1):
            ans.append(left[i - 1] * right[i + 1])
        ans.append(left[-2])
        
        return ans