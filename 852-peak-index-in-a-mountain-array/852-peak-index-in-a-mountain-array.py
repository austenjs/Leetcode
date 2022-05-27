class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle - 1
        return middle
                