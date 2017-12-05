# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # go through the intervals sorted by start coordinate and
    # either combine the current interval with the previous one
    # if they overlap, or add it to the output by itself if they don't.
    # beats 52.65%
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out