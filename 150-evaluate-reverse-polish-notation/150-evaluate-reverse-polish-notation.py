import math

class Solution:
    def __init__(self):
        self.operators = {"+", "-", "*", "/"}
        self.operator_to_function = {"+" : (lambda x, y : x + y),
                                     "-" : (lambda x, y : x - y),
                                    "*" : (lambda x, y : x * y),
                                    "/" : (lambda x, y : int(x / y))}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not self.is_operator(token):
                new_num = int(token)
            else:
                y, x = stack.pop(), stack.pop()
                new_num = self.get_operator(token)(x, y)
            stack.append(new_num)
        return stack.pop()
        
    def is_operator(self, token):
        return token in self.operators
    
    def get_operator(self, token):
        return self.operator_to_function[token]
