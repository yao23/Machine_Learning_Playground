# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import collections


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int

        beats 66.88%
        """
        if len(points) <= 2:
            return len(points)
        d = collections.defaultdict(int)  # (x,y) : count
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap = 0
            cur_max = 0
            for j in range(i+1, len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = self.get_gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx, dy)] += 1
                cur_max = max(cur_max, d[(dx, dy)])
            result = max(result, cur_max+overlap+1)
        return result

    def get_gcd(self, a, b):
        if b == 0:
            return a
        return self.get_gcd(b, a % b)
