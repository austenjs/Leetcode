class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        prev_end = None
        for start, end in sorted_intervals:
            if prev_end is None:
                prev_end = end
                continue
            if start < prev_end:
                return False
            prev_end = end
        return True
            