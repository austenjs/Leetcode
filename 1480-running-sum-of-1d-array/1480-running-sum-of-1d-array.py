class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cur = 0
        for num in nums:
            cur += num
            ans.append(cur)
        return ans