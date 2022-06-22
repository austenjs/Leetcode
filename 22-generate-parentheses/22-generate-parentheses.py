class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        
        ans = []
        added = set()

        # Previous
        candidates = self.generateParenthesis(n - 1)
        for candidate in candidates:
            new_string = '(' + candidate + ')'
            ans.append(new_string)
            added.add(new_string)
        
        for i in range(1, n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n - i)
            
            for l in left:
                for r in right:
                    new_string = l + r
                    if new_string in added:
                        continue
                    ans.append(new_string)
                    added.add(new_string)
        return ans