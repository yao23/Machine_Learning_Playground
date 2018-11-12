class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int

        beats 46.47%
        """
        def liss(envelopes):
            def lmip(envelopes, tails, k):
                b, e = 0, len(tails) - 1
                while b <= e:
                    m = (b + e) >> 1
                    if envelopes[tails[m]][1] >= k[1]:
                        e = m - 1
                    else:
                        b = m + 1
                return b

            tails = []
            for i, env in enumerate(envelopes):
                idx = lmip(envelopes, tails, env)
                if idx >= len(tails):
                    tails.append(i)
                else:
                    tails[idx] = i
            return len(tails)

        def f(x, y):
            return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1

        envelopes.sort(cmp=f)
        return liss(envelopes)
