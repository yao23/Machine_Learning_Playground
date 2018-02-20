class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        beats 41.93%
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid
            else:
                left = mid + 1
