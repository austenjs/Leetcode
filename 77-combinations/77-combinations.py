class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.generate(1, n, k)
        
    def generate(self, start, end, k):
        if k == 1:
            return [[i] for i in range(start, end + 1)]
        
        ans = []
        for begin in range(start, end + 1):
            to_merge = self.generate(begin + 1, end, k - 1)
            for item in to_merge:
                ans.append([begin] + item)
        
        return ans