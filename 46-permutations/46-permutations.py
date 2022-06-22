class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        list_of_indices = self.generate_index(len(nums))
        for indice in list_of_indices:
            cur = []
            for index in indice:
                cur.append(nums[index])
            ans.append(cur)
        return ans

    def generate_index(self, N):
        if N == 1:
            return [[0]]
        new_index = N - 1
        prev_indices = self.generate_index(N - 1)
        
        ans = []
        for indice in prev_indices:
            for i in range(len(indice) + 1):
                new_indice = indice.copy()
                new_indice.insert(i, new_index)
                ans.append(new_indice)
        return ans