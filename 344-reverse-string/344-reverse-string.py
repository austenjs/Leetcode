class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
    
    def reverse(self, s, i, j):
        if i >= j:
            return
        s[i], s[j] = s[j], s[i]
        self.reverse(s, i + 1, j - 1)