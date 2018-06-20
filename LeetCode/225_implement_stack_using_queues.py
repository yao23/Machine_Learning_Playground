import collections


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.

        beats 35.88%
        """
        self._queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self._queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
