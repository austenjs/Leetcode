class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return [[]] + self.non_empty_subset(nums)
        
    def non_empty_subset(self, nums):
        N = len(nums)
        if N <= 1:
            return [nums]
        subset1 = self.non_empty_subset(nums[:N // 2])
        subset2 = self.non_empty_subset(nums[N // 2:])
        return self.combine(subset1, subset2)
        
    def combine(self, subset1, subset2):
        ans = []
        for i in range(len(subset1)):
            for j in range(len(subset2)):
                ans.append(subset1[i] + subset2[j])
        return subset1 + subset2 + ans