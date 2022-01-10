class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        pivot = nums[0]
        left = []
        right = []
        for i in range(1, len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        if len(right) == k - 1:
            return pivot
        elif len(right) >= k:
            return self.findKthLargest(right, k)
        else:
            return self.findKthLargest(left, k - len(right) - 1)