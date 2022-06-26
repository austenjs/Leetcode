class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = self.find_min_index(nums)
        right = left + N - 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = nums[mid % N]
            if cur == target:
                return mid % N
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def find_min_index(self, nums : List[int]):
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[(mid + 1) % N]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[(mid + 1) % N]:
                return (mid + 1) % N
            elif nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return left % N