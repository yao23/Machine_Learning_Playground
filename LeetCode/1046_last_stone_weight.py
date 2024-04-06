class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=B-QCq79-Vfw
        
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
