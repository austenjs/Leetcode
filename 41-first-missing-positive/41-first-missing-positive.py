class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num > 0:
                hashset.add(num)
        for i in range(1, max(max(nums) + 2, 2)):
            if i not in hashset:
                return i