class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        ans = []
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans.append(nums[i] * nums[i])
                i += 1
            else:
                ans.append(nums[j] * nums[j])
                j -= 1
        return ans[::-1]