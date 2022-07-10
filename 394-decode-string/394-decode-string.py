class Solution:
    def decodeString(self, s: str) -> str:
        p = 0
        N = len(s)
        stack = ['']
        i = N - 1
        while i >= 0:
            if s[i] == ']':
                stack.append('')
            elif s[i] == '[':
                cur = ''
                to_add = stack.pop()
                while to_add:
                    cur += to_add
                    to_add = stack.pop()
                stack.append(cur)
            elif s[i] >= '0' and s[i] <= '9':
                cur = stack.pop()
                digits = s[i]
                i -= 1
                while i >= 0 and s[i] >= '0' and s[i] <= '9':
                    digits += s[i]
                    i -= 1
                for _ in range(int(digits[::-1])):
                    stack.append(cur)
                continue
            else:
                stack.append(s[i])
            i -= 1
        ans = ''
        for s in reversed(stack):
            ans += s
        return ans