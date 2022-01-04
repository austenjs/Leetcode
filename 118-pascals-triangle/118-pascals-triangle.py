class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1]]
        for index in range(numRows - 1):
            new_arr = []
            current = 0
            for i in range(len(ans[index])):
                new_arr.append(current + ans[index][i])
                current = ans[index][i]
            new_arr.append(1)
            ans.append(new_arr)
        return ans