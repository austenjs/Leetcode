from math import ceil, log

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        change = True

        for _ in range(ceil(log(N))):
            if not change:
                break
            change = False
            i = 0
            while i < N:
                num = nums[i]
                target_index = num - 1
                if i == target_index:
                    i += 1
                    continue
                tmp = nums[target_index]
                nums[target_index] = nums[i]
                nums[i] = tmp
                i += 1
                change = True

        ans = []
        for i in range(1, N + 1):
            if nums[i - 1] != i:
                ans.append(i)
        return ans