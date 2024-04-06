class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        https://www.youtube.com/watch?v=U2SozAs9RzA

        beats 16.02%
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h: # there could be smaller in left part
                res = k
                r = k - 1
            else: # need larger k
                l = k + 1
        return res
