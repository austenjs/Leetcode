class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters) - 1
        left, right = 0, N
        ans = ""
        while left <= right:
            middle = left + (right - left) // 2
            if letters[middle] > target:
                ans = letters[middle]
                right = middle - 1
            else:
                left = middle + 1
        return ans if ans else letters[middle % N]