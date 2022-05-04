from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        indices = self.generate_index(N)
        ans = []
        for index in indices:
            tmp = []
            for i in index:
                tmp.append(nums[i])
            ans.append(tmp)
        return ans

    def generate_index(self, N):
        if N == 1:
            return [[0]]
        ans = []
        children = self.generate_index(N - 1)
        new_index = N - 1
        for child in children:
            for i in range(len(child) + 1):
                tmp = child.copy()
                tmp.insert(i, new_index)
                ans.append(tmp)
        return ans
            