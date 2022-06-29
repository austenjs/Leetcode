class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        possible_sums = set([0])
        for num in nums:
            new_sums = set()
            for t in possible_sums:
                new_sums.add(t + num)
            possible_sums = possible_sums.union(new_sums)
            
        return target in possible_sums