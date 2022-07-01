from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        exist_single_char = False
        
        for val in count.values():
            if val % 2 == 1:
                exist_single_char = True
                ans += val - 1
            else:
                ans += val
        
        return ans + exist_single_char