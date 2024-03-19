class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=NMP3nRPyX5g&list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&index=10
        
        beats 42.68%
        """
        def isSubseq(s, subseq):
            i1, i2 = 0, 0

            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(subseq)

        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[:m + 1]) 
            if isSubseq(s, p):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1
        return res
