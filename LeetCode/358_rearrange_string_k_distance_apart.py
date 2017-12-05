import collections
import heapq

class Solution(object):
    # beats 48.46%
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        h = [(-freq, ch) for (ch, freq) in collections.Counter(s).items()]
        heapq.heapify(h)
        res = []
        while len(res) < len(s):
            q = []
            for _ in xrange(k):
                if len(res) == len(s):
                    return ''.join(res)
                if not h:
                    return ''
                freq, ch = heapq.heappop(h)
                res.append(ch)
                if freq < -1:
                    q.append((freq+1, ch))
            while q:
                heapq.heappush(h, q.pop())
        return ''.join(res)