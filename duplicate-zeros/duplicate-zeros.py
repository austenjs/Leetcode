class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        tmp = []
        N = len(arr)
        for i, num in enumerate(arr):
            if len(tmp) >= N:
                break
            if num == 0:
                tmp.append(0)
            tmp.append(num)
        
        for i in range(N):
            arr[i] = tmp[i]