class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i, num in enumerate(nums):
            if num not in seen:
                pass
            elif i - seen[num] <= k:
                return True
            seen[num] = i
        
        return False