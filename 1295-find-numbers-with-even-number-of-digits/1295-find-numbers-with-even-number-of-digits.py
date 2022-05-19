class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if self.getLength(num) % 2 == 0:
                ans += 1
        return ans
                
        
    def getLength(self, num):
        if num < 10:
            return 1
        elif num < 100:
            return 2
        elif num < 1000:
            return 3
        elif num < 10000:
            return 4
        elif num < 100000:
            return 5
        return 6