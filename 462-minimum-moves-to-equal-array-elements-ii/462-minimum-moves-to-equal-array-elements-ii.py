from collections import defaultdict

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            using_left = self.calculate(nums, mid - 1)
            using_mid = self.calculate(nums, mid)
            using_right = self.calculate(nums, mid + 1)
            
            if using_mid <= using_left and using_mid <= using_right:
                return using_mid
            elif using_mid > using_left:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.calculate(nums, left)
    
    def calculate(self, nums, target_elem):
        ans = 0
        for num in nums:
            ans += abs(num - target_elem)
        return ans