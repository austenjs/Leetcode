from math import ceil, log

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            tmp = nums[abs(num) - 1]
            if tmp < 0:
                continue
            nums[abs(num) - 1] = -tmp
        ans = []
        
        for i, num in enumerate(nums):
            if num < 0:
                continue
            ans.append(i + 1)
        return ans