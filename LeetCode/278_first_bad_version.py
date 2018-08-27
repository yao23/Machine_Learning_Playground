# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import bisect


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        beats 8.16%
        """
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)
