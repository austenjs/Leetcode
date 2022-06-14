class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)

        maximum_index = 0
        max_value = 0
        
        for i, num in enumerate(arr):
            if num > max_value:
                max_value = num
                maximum_index = i

        if maximum_index == 0 or maximum_index == N - 1:
            return False

        for i in range(1, maximum_index):
            if arr[i] <= arr[i - 1]:
                return False
        for j in range(maximum_index, N - 1):
            if arr[j] <= arr[j + 1]:
                return False
        
        return True