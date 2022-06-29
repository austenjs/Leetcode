from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        ans = []
        for key, val in counter1.items():
            if key not in counter2:
                continue
            for i in range(min(val, counter2[key])):
                ans.append(key)
        return ans