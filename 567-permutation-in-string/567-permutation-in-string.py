from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = len(s1)
        S2 = len(s2)
        counter_1 = Counter(s1)
        counter_2 = defaultdict(int)
        for char in s2[:S1]:
            counter_2[char] += 1

        left, right = 0, S1
        while right < S2:
            is_same = True
            for char, val in counter_1.items():
                if char not in counter_2 or counter_2[char] != val:
                    is_same = False
                    break
            if is_same:
                return True
            counter_2[s2[left]] -= 1
            counter_2[s2[right]] += 1
            left += 1
            right += 1
        is_same = True
        for char, val in counter_1.items():
            if char not in counter_2 or counter_2[char] != val:
                is_same = False
                break
        return is_same