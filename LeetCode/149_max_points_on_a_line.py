# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import collections

class Solution(object):
    # beats 66.88%
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2: return len(points)
        d = collections.defaultdict(int) # (x,y) : count
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap = 0
            curmax = 0
            for j in range(i+1, len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = self.getGcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx,dy)] += 1
                curmax = max(curmax, d[(dx,dy)])
            result = max(result, curmax+overlap+1)
        return result

    def getGcd(self, a, b):
        if b == 0: return a
        return self.getGcd(b, a%b)