import math

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            ans = [self.polynomial(x, a, b, c) for x in nums]
            return ans if b > 0 else ans[::-1]
        mid = -b / (2 * a)
        N = len(nums)
        index = closest = math.inf
        for i, num in enumerate(nums):
            dist = abs(num - mid)
            if dist < closest:
                closest = dist
                index = i        
        ans = [self.polynomial(nums[index], a, b, c)]
        
        left, right = index - 1, index + 1
        while left >= 0 and right < N:
            if abs(nums[left]  - mid) > abs(nums[right] - mid):
                ans.append(self.polynomial(nums[right], a, b, c))
                right += 1
            else:
                ans.append(self.polynomial(nums[left], a, b, c))
                left -= 1
        
        while left >= 0:
            ans.append(self.polynomial(nums[left], a, b, c))
            left -= 1
        while right < N:
            ans.append(self.polynomial(nums[right], a, b, c))
            right += 1
        return ans if a > 0 else ans[::-1]
    
    def polynomial(self, x, a, b, c):
        return a * x * x + b * x + c