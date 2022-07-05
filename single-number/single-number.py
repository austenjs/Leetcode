from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use XOR as a ^ a = 0
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans