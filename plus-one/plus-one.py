class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] != 10:
            return digits
        i = len(digits) - 1
        while i > 0:
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i - 1] += 1
            i -= 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits
            