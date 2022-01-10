from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        count = Counter(nums)
        if len(count) == k:
            return list(count.keys())
        pair_of_nums_and_freq = [(num, count[num]) for num in count.keys()]
        top_k = self.quickSelect(pair_of_nums_and_freq, k)
        return list(map(lambda x: x[0], top_k))
    
    def quickSelect(self, pair_of_nums_and_freq, k):
        if len(pair_of_nums_and_freq) == 1:
            return [pair_of_nums_and_freq[0]]
        pivot = pair_of_nums_and_freq[len(pair_of_nums_and_freq) // 2]
        left = []
        right = []
        for pair in pair_of_nums_and_freq:
            if pair[0] == pivot[0]:
                continue
            elif pair[1] > pivot[1]:
                right.append(pair)
            else:
                left.append(pair)
        if len(right) == k:
            return right
        elif len(right) == k - 1:
            right.append(pivot)
            return right
        elif len(right) < k:
            right.append(pivot)
            return right + self.quickSelect(left, k - len(right))
        else:
            return self.quickSelect(right, k)