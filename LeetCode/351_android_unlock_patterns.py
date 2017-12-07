import re

class Solution(object):
    # beats 51.88%
    def numberOfPatterns(self, m, n, patterns=[['']]):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while len(patterns) <= n:
            bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
            bad = re.compile(bad).match
            patterns += [p+d for p in patterns[-1] for d in '123456789'
                         if d not in p and not bad(p+d)],
        return sum(map(len, patterns[m:n+1]))

    def numberOfPatterns1(self, m, n, patterns=[]):
        while len(patterns) <= n:
            bad = '[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
            bad = re.compile(bad).match
            patterns += sum(not bad(''.join(p))
                            for p in itertools.permutations('123456789', len(patterns))),
        return sum(patterns[m:n + 1])