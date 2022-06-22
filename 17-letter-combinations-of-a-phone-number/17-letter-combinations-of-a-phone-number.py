class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        N = len(digits)
        def backtrack(i = 0, cur = []):
            if i == N:
                return cur
            candidates = mapping[digits[i]]
            if len(cur) == 0:
                new_cur = [candidate for candidate in candidates]
            else:
                new_cur = []
                for c in cur:
                    for candidate in candidates:
                        new_cur.append(c + candidate)
            return backtrack(i + 1, new_cur)
        
        output = backtrack()
        return output