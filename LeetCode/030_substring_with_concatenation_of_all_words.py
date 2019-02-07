class Solution(object):
    def _findSubstring(self, left, right, n, k, t, s, req, ans):
        curr = {}
        while right + k <= n:
            w = s[right:right + k]
            right += k
            if w not in req:
                left = right
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[left:left + k]] -= 1
                    left += k
                if right - left == t:
                    ans.append(left)

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]

        beats 82.05%
        """
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in xrange(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans
