class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        right = values[-1] - N + 1
        
        ans = 0
        for i in range(N - 2, -1, -1):
            ans = max(ans, values[i] + i + right)
            right = max(right, values[i] - i)
        return ans