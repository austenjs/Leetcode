class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        ans.append(intervals[0])
        
        idx = 1
        N = len(intervals)
        while idx < N:
            cur = intervals[idx]
            start, end = cur
            if ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append(cur)
            idx += 1
        return ans