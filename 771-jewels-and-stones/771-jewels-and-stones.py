from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        type_to_count = Counter(stones)
        return sum(map(lambda char : type_to_count[char], jewels))