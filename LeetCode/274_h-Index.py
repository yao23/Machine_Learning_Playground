class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int

        beats 57.86%
        """
        n = len(citations)
        cite_count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                cite_count[n] += 1
            else:
                cite_count[c] += 1

        i = n - 1
        while i >= 0:
            cite_count[i] += cite_count[i + 1]
            if cite_count[i + 1] >= i + 1:
                return i + 1
            i -= 1
        return 0
