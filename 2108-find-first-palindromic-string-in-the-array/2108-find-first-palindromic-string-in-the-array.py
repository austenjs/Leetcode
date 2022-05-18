class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.checkPalindrome(word):
                return word
        return ""
        
    def checkPalindrome(self, string):
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True