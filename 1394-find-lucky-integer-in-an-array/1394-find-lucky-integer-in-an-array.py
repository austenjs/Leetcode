from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        largest = -1
        for num in counter.keys():
            if counter[num] == num:
                largest = max(largest, num)
        return largest