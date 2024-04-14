class Solution:
    """
    https://www.youtube.com/watch?v=1IUzNJ6TPEM
    
    beats 61.79%
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(c, p) for c,p in zip(capital, profits)]
        heapq.heapify(minHeap)
        maxProfit = [] # only projects we can afford

        for i in range(k):
            while minHeap and minHeap[0][0] <= w: # able to take the project with min capital
                c, p = heapq.heappop(minHeap)
                heapq.heappush(maxProfit, -p) # push profit of the project 

            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit) # get max profit
        return w
