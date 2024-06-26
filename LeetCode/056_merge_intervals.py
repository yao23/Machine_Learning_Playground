class Interval(object):
    """
    Definition for an interval.
    """
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

        go through the intervals sorted by start coordinate and either combine the current interval with the previous
        one if they overlap, or add it to the output by itself if they don't.

        beats 52.65%
        """
        out = []
        for i in sorted(intervals, key=lambda interval: interval.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
