class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        beats 99.69%
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
