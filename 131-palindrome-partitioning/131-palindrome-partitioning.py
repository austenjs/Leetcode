class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        def backtrack(start = 0, cur = []):
            if start == N:
                ans.append(cur.copy())
                return
            for end in range(start, N):
                if self.is_palindrome(s, start, end):
                    cur.append(s[start:end + 1])
                    backtrack(end + 1, cur)
                    cur.pop()
        
        ans = []
        backtrack()
        return ans
    
    def is_palindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True