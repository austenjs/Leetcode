class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        for i, char in enumerate(s):
            if char in mapping_s_to_t and t[i] != mapping_s_to_t[char]:
                return False
            if t[i] in mapping_t_to_s and mapping_t_to_s[t[i]] != char:
                return False
            mapping_s_to_t[char] = t[i]
            mapping_t_to_s[t[i]] = char
        return True