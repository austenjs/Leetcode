class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        if target in nums:
            return True
        
        dp = set([0])
        for num in reversed(nums):
            new_dp = set()
            for t in dp:
                if t + num == target:
                    return True
                new_dp.add(t + num)
            dp = dp.union(new_dp)
        
        return target in dp
        
        