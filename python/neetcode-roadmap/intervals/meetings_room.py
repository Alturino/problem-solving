from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if prevEnd > start:
                return False
            prevEnd = end
        return True
