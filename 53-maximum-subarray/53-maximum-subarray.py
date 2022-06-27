import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        ans = -math.inf
        for num in nums:
            cur += num
            ans = max(ans, cur)
            if cur < 0:
                cur = 0
        return ans
        