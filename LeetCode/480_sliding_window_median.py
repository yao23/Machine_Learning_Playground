class Solution:
    """
    https://www.youtube.com/watch?v=oKwmSnmEFpY
    
    beats 69.86%
    """
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap, minHeap = [], []
        heapDict = collections.defaultdict(int)

        res = []

        def getMedian():
            if k % 2 == 1:
                median = -maxHeap[0]
            else:
                median = (-maxHeap[0] + minHeap[0]) / 2
            res.append(median)
            return median

        def removeHeapTopNum(hp, isMaxHeap):
            if len(hp):
                top = -hp[0] if isMaxHeap else hp[0]
                while hp and heapDict[top] > 0:
                    heapDict[top] -= 1
                    heapq.heappop(hp)
                    top = -hp[0] if isMaxHeap else hp[0]
        
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            if len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        median = getMedian()
        
        for i in range(k, len(nums)):
            prevNum = nums[i - k]
            heapDict[prevNum] += 1
            balance = -1 if prevNum <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(maxHeap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(minHeap, nums[i])

            if balance < 0:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            elif balance > 0:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            # while maxHeap and heapDict[-maxHeap[0]] > 0:
            #     heapDict[-maxHeap[0]] -= 1
            #     heapq.heappop(maxHeap)

            # while minHeap and heapDict[minHeap[0]] > 0:
            #     heapDict[minHeap[0]] -= 1
            #     heapq.heappop(minHeap)

            # extract above 2 while logic to the below function
            removeHeapTopNum(maxHeap, True)
            removeHeapTopNum(minHeap, False)

            median = getMedian()
        return res
