class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_pointer = 0
        right_pointer = 0
        len_s = len(s)
        len_t = len(t)
        while left_pointer < len_s and right_pointer < len_t:
            if s[left_pointer] == t[right_pointer]:
                left_pointer += 1
            right_pointer += 1
        return left_pointer == len_s