class Solution:
    def __init__(self):
        self.mapping = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        self.double_pair = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}

    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return self.mapping[s]

        first_two_chars = s[:2]
        if first_two_chars in self.double_pair:
            return self.double_pair[first_two_chars] + self.romanToInt(s[2:])
        
        return self.mapping[s[0]] + self.romanToInt(s[1:])