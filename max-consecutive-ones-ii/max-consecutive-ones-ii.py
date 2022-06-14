class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = cur = ans = 0
        all_zeroes = all_ones = True
        
        for num in nums:
            if num == 1:
                cur += 1
                all_zeroes = False
            else:
                all_ones = False
                ans = max(ans, prev + cur + 1)
                prev = cur
                cur = 0

        if all_ones:
            return cur
        if all_zeroes:
            return 1

        ans = max(ans, prev + cur + 1)
        return ans