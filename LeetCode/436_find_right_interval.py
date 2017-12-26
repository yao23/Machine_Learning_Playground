# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import bisect


class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]

        For each end point search for the first start point that is equal or higher in a previously constructed ordered
        list of start points. If there is one then return its index. If not return -1

        beats 71.43%
        """
        ordered_list = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(ordered_list, (e.end,))  # like TreeMap ceilingKey in Java
            res.append(ordered_list[r][1] if r < len(ordered_list) else -1)
        return res
