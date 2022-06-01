from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        for num, val in ransom_count.items():
            if num not in mag_count or val > mag_count[num]:
                return False
        return True