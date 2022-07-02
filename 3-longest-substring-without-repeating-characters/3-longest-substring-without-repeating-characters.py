class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        ans = 0
        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
                continue
            prev = seen[char]
            if prev < left:
                pass
            else:
                cur = i - left
                ans = cur if cur > ans else ans
                left = prev + 1
            seen[char] = i
        cur = len(s) - left
        ans = cur if cur > ans else ans
        return ans