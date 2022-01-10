class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        ans = 0
        for char in s:
            if char == '(':
                stack += 1
                ans = max(ans, stack)
            elif char == ')':
                stack -= 1
        return ans