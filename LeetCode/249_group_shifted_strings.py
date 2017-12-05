class Solution(object):
    # beats 46.08%
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
        return [list(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]