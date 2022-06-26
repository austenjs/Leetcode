class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == 0:
            return 0
        N = len(cardPoints)
        if N == k:
            return sum(cardPoints)
        
        cur = sum(cardPoints[:k])
        left_pointer = k - 1
        right_pointer = N - 1
        
        ans = cur
        while left_pointer >= 0:
            cur = cur - cardPoints[left_pointer] + cardPoints[right_pointer]
            ans = max(ans, cur)
            left_pointer -= 1
            right_pointer -= 1
        return ans