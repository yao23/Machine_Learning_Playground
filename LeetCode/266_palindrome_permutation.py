import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        beats 49.02%
        """
        return sum(v % 2 for v in collections.Counter(s).values()) < 2
