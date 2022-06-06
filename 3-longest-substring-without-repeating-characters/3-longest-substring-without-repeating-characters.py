class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        ans = 0
        left = 0
        for i, char in enumerate(s):
            # Unseen
            if char not in char_to_index:
                char_to_index[char] = i
                continue

            prev_index = char_to_index[char]
            if prev_index < left:
                pass
            else:
                cur = i - left
                ans = cur if cur > ans else ans
                left = prev_index + 1
            char_to_index[char] = i
        cur = len(s) - left
        ans = cur if cur > ans else ans
        return ans