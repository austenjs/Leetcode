class Solution:
    def __init__(self):
        self.palindrome_list = set()
        self.str_to_list = defaultdict()

    def partition(self, s: str) -> List[List[str]]:
        if s in self.str_to_list:
            return self.str_to_list[s]

        N = len(s)
        if N == 0:
            return [[]]
        if N == 1:
            return [[s]]
        if N == 2:
            ans = [[s[0], s[1]]]
            if s[0] == s[1]:
                ans.append([s])
            self.str_to_list[s] = ans
            return ans
        unique = set()
        for i in range(1, N):
            left = self.partition(s[:i])
            right = self.partition(s[i:])
            for l in left:
                for r in right:
                    unique.add(tuple(l + r))
        ans = [[*items] for items in unique]
        
        if self.is_palindrome(s):
            ans.append([s])
        self.str_to_list[s] = ans
        return ans
    
    def is_palindrome(self, s):
        if s in self.palindrome_list:
            return True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        self.palindrome_list.add(s)
        return True