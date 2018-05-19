class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        beats 74.68%
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i + (1 if len(s) >= len(t) else 0):] == t[i + (1 if len(s) <= len(t) else 0):]
        return abs(len(s) - len(t)) == 1
