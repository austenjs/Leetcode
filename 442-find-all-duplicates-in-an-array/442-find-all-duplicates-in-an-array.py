class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            num = num if num > 0 else -num
            if nums[num - 1] < 0:
                ans.append(num)
            nums[num - 1] *= -1
        
        return ans