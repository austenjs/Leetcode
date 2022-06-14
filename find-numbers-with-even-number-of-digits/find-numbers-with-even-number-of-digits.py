import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if self.getLength(num) % 2 == 0:
                ans += 1
        return ans
                
        
    def getLength(self, num):
        if num == 0:
            return 1
        return math.floor(math.log10(num)) + 1