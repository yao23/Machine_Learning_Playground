import collections


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int

        beats 56.30%
        """
        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
