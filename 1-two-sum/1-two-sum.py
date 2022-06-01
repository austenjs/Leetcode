class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in visited:
                visited.add(num)
                continue
            for j in range(i):
                if nums[j] == complement:
                    return [i, j]