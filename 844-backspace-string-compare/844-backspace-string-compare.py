import itertools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return all(x == y for x, y in itertools.zip_longest(self.stringBuilder(s), self.stringBuilder(t)))
    
    def stringBuilder(self, s):
        skip = 0
        for char in reversed(s):
            if char == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char
