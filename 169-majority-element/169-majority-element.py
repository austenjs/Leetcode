from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        counter = Counter(nums)
        for key, val in counter.items():
            if val > N // 2:
                return key
        return -1