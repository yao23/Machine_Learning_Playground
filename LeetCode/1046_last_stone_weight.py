class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        beats 11.00%
        """
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, (-1 * s))

        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap) * (-1)
            b = heapq.heappop(maxHeap) * (-1)
            if a > b:
                heapq.heappush(maxHeap, (-1 * (a - b)))

        return maxHeap[0] * -1 if len(maxHeap) == 1 else 0

    def lastStoneWeightV0(self, stones: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=B-QCq79-Vfw
        
        beats 54.78
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

    def lastStoneWeightV1(self, stones: List[int]) -> int:
        """
        # There's a private _heapify_max method.
        # https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
        """
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)
        
        stones.append(0)
        return stones[0]
