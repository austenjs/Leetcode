class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        ans = 0
        for word in words:
            valid = True
            for char in word:
                if char not in allowed_chars:
                    valid = False
                    break
            ans += valid
        return ans
                