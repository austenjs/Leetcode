class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = 0
        right = N - 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = nums[mid]
            if cur == target:
                return mid
            elif cur >= nums[left]:
                if target >= nums[left] and target < cur:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > cur:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return -1
    