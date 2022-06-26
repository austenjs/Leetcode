class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[(mid + 1) % N]:
                return nums[mid]
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[(mid + 1) % N]:
                return nums[(mid + 1) % N]
            elif nums[left] > nums[right]:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
             
        return nums[left]