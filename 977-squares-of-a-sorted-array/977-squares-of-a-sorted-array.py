class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid_index = self.binarySearch(nums)
        left = self.allNegative(nums[:mid_index]) 
        right = self.allPositive(nums[mid_index:])
        ans = []
        i = j = 0
        M, N = len(left), len(right)
        while i < M and j < N:
            if left[i] > right[j]:
                ans.append(right[j])
                j += 1
            else:
                ans.append(left[i])
                i += 1
        while i < M:
            ans.append(left[i])
            i += 1
        while j < N:
            ans.append(right[j])
            j += 1
        return ans
    
    def allNegative(self, nums):
        ans = []
        for num in reversed(nums):
            ans.append(num * num)
        return ans
        
    def allPositive(self, nums):
        ans = []
        for num in nums:
            ans.append(num * num)
        return ans
        
    def binarySearch(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] == 0:
                return middle
            elif nums[middle] > 0:
                right = middle
            else:
                left = middle + 1
        return right