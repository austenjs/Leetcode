class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0
        
        S, T = len(s), len(t)
        
        while pointer_s < S and pointer_t < T:
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
            
        return pointer_s == S