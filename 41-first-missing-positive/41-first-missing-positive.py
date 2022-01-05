class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set()
        max_num = 2
        for num in nums:
            if num > 0:
                hashset.add(num)
                max_num = max(num, max_num)
        for i in range(1, max_num + 2):
            if i not in hashset:
                return i