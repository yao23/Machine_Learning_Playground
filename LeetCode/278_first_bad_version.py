# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    # beats 8.16%
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)