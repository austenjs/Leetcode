class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left_parantheses = {'(', '{', '['}
        complement_parantheses = {')' : '(', '}' : '{', ']' : '['}
        for char in s:
            if char in left_parantheses:
                stack.append(char)
                continue
            elif len(stack) == 0:
                return False
            elif stack[-1] != complement_parantheses[char]:
                return False
            stack.pop()
        return len(stack) == 0
                