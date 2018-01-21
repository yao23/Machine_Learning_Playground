import itertools


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str

        beats 6.52%
        """
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s
