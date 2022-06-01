class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = []
        for char in s:
            if char.isalnum():
                new_s.append(char.lower())
        
        left, right = 0, len(new_s) - 1
        
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True