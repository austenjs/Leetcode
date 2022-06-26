class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        N = len(intervals)
        
        # Non-overlapping section
        i = 0
        
        while i < N:
            cur = intervals[i]
            if self.is_overlapping(cur, newInterval):
                break
            if cur[0] > newInterval[1]:
                break
            ans.append(intervals[i])
            i += 1
        
        print(ans, intervals)
        if i == N:
            ans.append(newInterval)
            return ans
        
        if i == 0:
            if len(intervals) == 0:
                return [newInterval]
            elif self.is_overlapping(intervals[0], newInterval):
                combined = self.combine(intervals[0], newInterval)
                i = 1
                while i < N and self.is_overlapping(combined, intervals[i]):
                    combined = self.combine(combined, intervals[i])
                    i += 1
                ans.append(combined)
                while i < N:
                    ans.append(intervals[i])
                    i += 1
                return ans
            else:
                ans.append(newInterval)
                return ans + intervals

        if not self.is_overlapping(cur, newInterval):
            return intervals[:i] + [newInterval] + intervals[i:]
        
        combined = self.combine(intervals[i], newInterval)
        
        i += 1
        while i < N and self.is_overlapping(combined, intervals[i]):
            combined = self.combine(combined, intervals[i])
            i += 1
        ans.append(combined)

        while i < N:
            ans.append(intervals[i])
            i += 1
        
        return ans
    
    def is_overlapping(self, interval1, interval2):
        if interval1[0] > interval2[0]:
            return interval1[0] <= interval2[1]
        else:
            return interval1[1] >= interval2[0]
    
    def combine(self, interval1, interval2):
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]