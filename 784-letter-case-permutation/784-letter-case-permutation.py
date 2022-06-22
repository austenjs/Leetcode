class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 0 or s.isnumeric():
            return [s]
        if len(s) == 1:
            return [s.capitalize(), s.casefold()]
        
        has_number = False
        index = len(s) // 2
        for i, char in enumerate(s):
            if char >= '0' and char <= '9':
                index = i
                has_number = True
                break
    
        if has_number:
            left = s[:index]
            right = s[index + 1:]
            connector = s[index]
        else:
            left = s[:index]
            right = s[index:]
            connector = ''
        
        ans = []
        candidates_left = self.letterCasePermutation(left)
        candidates_right = self.letterCasePermutation(right)
        
        if len(candidates_left) == 0:
            for r in candidates_right:
                ans.append(connector + r)
        elif len(candidates_right) == 0:
            for l in candidates_left:
                ans.append(l + connector)
        else:
            for l in candidates_left:
                for r in candidates_right:
                    ans.append(l + connector + r)
        
        return ans