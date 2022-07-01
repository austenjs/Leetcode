from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        num_pairs = 0
        unpaired_chars = set()
        
        for char in s:
            if char in unpaired_chars:
                num_pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        return num_pairs * 2 + 1 if unpaired_chars else num_pairs * 2