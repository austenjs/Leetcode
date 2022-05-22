class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # O(1) seek
        existing_nums = set(nums)
        
        ans = []
        for i in range(1, N + 1):
            if i not in existing_nums:
                ans.append(i)
        return ans