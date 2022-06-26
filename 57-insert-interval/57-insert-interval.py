class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        new_start, new_end = newInterval
        idx, N = 0, len(intervals)
        
        # Add intervals that start before newInterval
        while idx < N and new_start > intervals[idx][0]:
            ans.append(intervals[idx])
            idx += 1
        
        # Add newInterval
        if not ans or ans[-1][1] < new_start:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][1], new_end)
        
        # Add the rest
        while idx < N:
            cur = intervals[idx]
            start, end = cur
            if ans[-1][1] < start:
                ans.append(cur)
            else:
                ans[-1][1] = max(ans[-1][1], end)
            idx += 1
            
        return ans