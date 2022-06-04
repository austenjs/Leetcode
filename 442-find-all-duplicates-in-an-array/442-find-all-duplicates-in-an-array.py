class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        ans = []
        
        for num in nums:
            if num in visited:
                ans.append(num)
            visited.add(num)
    
        return ans