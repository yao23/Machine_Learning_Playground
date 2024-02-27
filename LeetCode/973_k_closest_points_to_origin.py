class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # https://walkccc.me/LeetCode/problems/0973/#__tabbed_3_3
    # https://github.com/yao23/Java_Playground/blob/master/src/com/leetcode/www/KClosestPointsToOrigin.java
    
    maxHeap = []

    for x, y in points:
      heapq.heappush(maxHeap, (- x * x - y * y, [x, y]))
      if len(maxHeap) > k:
        heapq.heappop(maxHeap)

    return [pair[1] for pair in maxHeap]
