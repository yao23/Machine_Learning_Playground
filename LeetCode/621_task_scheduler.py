class Solution:
  def leastIntervals(self, tasks: List[str], n: int) -> int:
    """
    :type tasks: List[int]
    :type n: int
    :rtype: int

    # beats 96.95%
    # FB
    """
    counter = Counter(tasks)
    maxHeap = [-cnt for cnt in counter.values()] # ready tasks' time
    heapq.heapify(maxHeap)
    time = 0
    queue = dequeue() # pending tasks' time and idle time, [-cnt, idle_time]
    
    while maxHeap or queue:
      time += 1 # current timestamp
      if maxHeap:
          cnt = 1 + heapq.heappop(maxHeap)
          if cnt:
              queue.append([cnt, time + n]) # pending tasks to process

      if queue and queue[0][1] == time: # suffcient idle time and ready to process task
          heapq.heappush(maxHeap, queue.popleft()[0])

    return time # finish processing all tasks
        


        
    
