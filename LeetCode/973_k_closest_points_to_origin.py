class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      """
      https://www.youtube.com/watch?v=rI2EBUEMfTk
      
      beats 65.80%
      """
      minHeap = []
      for x, y in points:
          dist = (x ** 2) + (y ** 2)
          minHeap.append((dist, x, y))
      
      heapq.heapify(minHeap)
      res = []
      for _ in range(k):
          _, x, y = heapq.heappop(minHeap)
          res.append((x, y))
      return res

  
  def kClosestV0(self, points: List[List[int]], k: int) -> List[List[int]]:
    # https://walkccc.me/LeetCode/problems/0973/#__tabbed_3_3
    # https://github.com/yao23/Java_Playground/blob/master/src/com/leetcode/www/KClosestPointsToOrigin.java
    
    maxHeap = []

    for x, y in points:
      heapq.heappush(maxHeap, (- x * x - y * y, [x, y]))
      if len(maxHeap) > k:
        heapq.heappop(maxHeap)

    return [pair[1] for pair in maxHeap]
