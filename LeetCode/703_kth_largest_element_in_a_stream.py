class KthLargest:
    """
    https://www.youtube.com/watch?v=hOjcdrqMoQ8
    
    beats 87.91%
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = [] # min heap with k largest number
        heapq.heapify(self.minHeap)
        for n in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap, n)
            else:
                if n > self.minHeap[0]: # compare with top element in min heap
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, n)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
