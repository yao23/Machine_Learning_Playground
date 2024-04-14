from heapq import *


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.

        beats 50.85%
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

class MedianFinderV0:
    """
    beats 20.71%
    """
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if len(self.maxHeap) < len(self.minHeap) - 1: # more number in minHeap
            cur = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, cur * (-1))
        if self.maxHeap and self.minHeap:
            if (self.maxHeap[0] * (-1)) > self.minHeap[0]: # maxHeap top element larger than minHeap
                tmp1 = heapq.heappop(self.maxHeap) * (-1) 
                tmp2 = heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, tmp1)
                heapq.heappush(self.maxHeap, tmp2 * (-1))

    def findMedian(self) -> float:
        if len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        else:
            return (self.maxHeap[0] * (-1) + self.minHeap[0]) / 2

class MedianFinderV1:
    def __init__(self):
        """
        initialize your data structure here.

        https://www.youtube.com/watch?v=itmhHWaHupI
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
