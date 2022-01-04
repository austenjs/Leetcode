class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            new_arr = [1]
            for k in range(len(ans) - 1):
                new_arr.append(ans[k] + ans[k + 1])
            new_arr.append(1)
            ans = new_arr
        return ans