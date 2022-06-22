class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        elif k == len(nums):
            return min(nums)

        N = len(nums)
        pivot = N // 2
        left = []
        right = []
        for i, num in enumerate(nums):
            if i == pivot:
                continue
            if num <= nums[pivot]:
                left.append(num)
            else:
                right.append(num)
        
        print(left, right, nums[pivot], k)
        if len(right) == 0:
            if k == 1:
                return nums[pivot]
            return self.findKthLargest(left, k - 1)
        
        if len(right) == k - 1:
            return nums[pivot]
        elif len(right) >= k:
            return self.findKthLargest(right, k)
        else:
            return self.findKthLargest(left, k - len(right) - 1)