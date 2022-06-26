import math

class Solution:
    def get_elem(self, index):
        if index == -1:
            return -math.inf
        elif index == len(self.nums):
            return -math.inf
        return self.nums[index]
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums = nums
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            left_val = self.get_elem(mid - 1)
            right_val = self.get_elem(mid + 1)
            cur = self.get_elem(mid)
            print(left_val, right_val)
            if cur > left_val and cur > right_val:
                return mid
            elif left_val > cur:
                right = mid - 1
            else:
                left = mid + 1
        return left
            