class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        for num in nums:
            if num == 0:
                cur = 0
            else:
                cur += 1
            ans = cur if cur > ans else ans
        return ans