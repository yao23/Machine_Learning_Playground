class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]

        beats 67.21%
        """
        r, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)
