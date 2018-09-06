class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool

        beats 83.67%
        """
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return f(pattern) == f(str.split())
