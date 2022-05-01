class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        stack_a = list(a)
        stack_b = list(b)
        ans = []
        while stack_a and stack_b:
            first, second = stack_a.pop(), stack_b.pop()
            if carry:
                if first == "1" and second == "1":
                    carry = 1
                    ans.append("1")
                elif first == "1" and second == "0":
                    carry = 1
                    ans.append("0")
                elif first == "0" and second == "1":
                    carry = 1
                    ans.append("0")
                else:
                    carry = 0
                    ans.append("1")
            else:
                if first == "1" and second == "1":
                    carry = 1
                    ans.append("0")
                elif first == "1" and second == "0":
                    carry = 0
                    ans.append("1")
                elif first == "0" and second == "1":
                    carry = 0
                    ans.append("1")
                else:
                    carry = 0
                    ans.append("0")
        while stack_a:
            item = stack_a.pop()
            if carry and item == "1":
                carry = 1
                ans.append("0")
            elif carry:
                carry = 0
                ans.append("1")
            else:
                ans.append(item)
        while stack_b:
            item = stack_b.pop()
            if carry and item == "1":
                carry = 1
                ans.append("0")
            elif carry:
                carry = 0
                ans.append("1")
            else:
                ans.append(item)
        if carry:
            ans.append("1")
        return "".join(ans[::-1])