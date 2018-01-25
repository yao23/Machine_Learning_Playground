from heapq import *


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]

        https://discuss.leetcode.com/topic/14987/108-ms-17-lines-body-explained/2

        It sweeps from left to right. But it doesn't only keep heights of "alive buildings" in the priority queue and
        it doesn't remove them as soon as their building is left behind. Instead, (height, right) pairs are kept in the
        priority queue and they stay in there as long as there's a larger height in there, not just until their building
        is left behind.

        In each loop, we first check what has the smaller x-coordinate: adding the next building from the input, or
        removing the next building from the queue. In case of a tie, adding buildings wins, as that guarantees
        correctness (think about it :-). We then either add all input buildings starting at that x-coordinate or we
        remove all queued buildings ending at that x-coordinate or earlier (remember we keep buildings in the queue as
        long as they're "under the roof" of a larger actually alive building). And then, if the current maximum height
        in the queue differs from the last in the skyline, we add it to the skyline.

        beats 93.68%
        """
        LRH = buildings
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
