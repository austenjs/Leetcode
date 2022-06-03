class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if self.min_val is None or val < self.min_val:
            self.min_val = val
        node = Node(val, self.min_val)
        self.stack.append(node)

    def pop(self) -> None:
        to_remove = self.stack.pop()
        if not self.stack:
            self.min_val = None
        else:
            self.min_val = self.stack[-1].get_min_val()

    def top(self) -> int:
        return self.stack[-1].get_val()

    def getMin(self) -> int:
        return self.stack[-1].get_min_val()

class Node:
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val
    
    def get_val(self):
        return self.val
    
    def get_min_val(self):
        return self.min_val
    
    def __str__(self):
        return f"({self.val}, {self.min_val})"

    def __unicode__(self):
        return u'a'

    def __repr__(self):
        return f"({self.val}, {self.min_val})"


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()