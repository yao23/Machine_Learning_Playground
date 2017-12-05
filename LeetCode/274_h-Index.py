class Solution(object):
    # beats 57.86%
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citeCount = [0] * (n + 1)
        for c in citations:
            if c >= n:
                citeCount[n] += 1
            else:
                citeCount[c] += 1

        i = n - 1
        while i >= 0:
            citeCount[i] += citeCount[i + 1]
            if citeCount[i + 1] >= i + 1:
                return i + 1
            i -= 1
        return 0