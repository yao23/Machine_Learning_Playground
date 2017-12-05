class Solution(object):
    # beats 83.67%
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return f(pattern) == f(str.split())