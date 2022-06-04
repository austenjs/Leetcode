class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        bins = [1 for _ in range(61)]
        offset = 30
        
        visited = set()
        
        for num in nums:
            for i in range(61):
                if i == num + offset and not num in visited:
                    continue
                bins[i] *= num
            visited.add(num)
        
        ans = []
        for num in nums:

            if not num in visited:
                ans.append(0)
            else:
                ans.append(bins[num + offset])
        return ans