from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i, num in enumerate(nums):
            if num > 0:
                continue
            if i == 0 or nums[i - 1] != num:
                self.addTriplet(nums, i, ans)
        
        return ans
    
    def addTriplet(self, nums, start, ans):
        left, right = start + 1, len(nums) - 1
        
        while left < right:
            total = nums[start] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                ans.append((nums[start], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1