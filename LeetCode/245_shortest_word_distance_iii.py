class Solution(object):
    # beats 98.20%
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(words)
        ans = n
        p1 = p2 = -n
        same = word1 == word2
        for i in xrange(n):
            if words[i] == word1:
                p1 = i
                ans = min(ans, i - p2)
                if same:
                    p2 = p1
            elif not same and words[i] == word2:
                p2 = i
                ans = min(ans, i - p1)
        return ans