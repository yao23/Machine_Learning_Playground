class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        # beats 86.80%
        """
        t = iter(t)
        return all(c in t for c in s)
