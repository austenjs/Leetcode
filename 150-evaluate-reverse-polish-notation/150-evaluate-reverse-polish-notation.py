import math

class Solution:
    def __init__(self):
        self.operators = {"+", "-", "*", "/"}
        self.operator_to_function = {"+" : (lambda x, y : x + y),
                                     "-" : (lambda x, y : x - y),
                                    "*" : (lambda x, y : x * y),
                                    "/" : (lambda x, y : self.custom_div(x, y))}
    
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

    def custom_div(self, num1, num2):
        if (num1 < 0 and num2 < 0) or (num1 > 0 and num2 > 0):
            return num1 // num2
        return math.ceil(num1 / num2)