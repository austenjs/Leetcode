class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            prev = ans[i - 1]
            new = [1]
            for j in range(1, len(prev)):
                new.append(prev[j] + prev[j - 1])
            new.append(1)
            ans.append(new)
            
        return ans[:numRows]