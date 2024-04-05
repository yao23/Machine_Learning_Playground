# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import bisect


class Solution(object):
    def firstBadVersion(self, n: int) -> int:
        """
        https://www.youtube.com/watch?v=KiZwKNpayZw
        
        beats 59.19%
        """
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
    
    def firstBadVersionV0(self, n):
        """
        :type n: int
        :rtype: int

        beats 8.16%
        """
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)
