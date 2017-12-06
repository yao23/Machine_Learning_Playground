class WordDistance(object):
    # beats 24.33%
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for i, w in enumerate(words):
            self.d[w] = self.d.get(w, []) + [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a, b = self.d[word1], self.d[word2]
        m, n, i, j, res = len(a), len(b), 0, 0, sys.maxsize
        while i < m and j < n:
            res = min(res, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)