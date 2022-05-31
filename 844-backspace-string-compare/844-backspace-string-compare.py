class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        true_s = []
        true_t = []
        
        for char in s:
            if char != '#':
                true_s.append(char)
            elif len(true_s):
                true_s.pop()
                
        for char in t:
            if char != '#':
                true_t.append(char)
            elif len(true_t):
                true_t.pop()
        
        return true_s == true_t