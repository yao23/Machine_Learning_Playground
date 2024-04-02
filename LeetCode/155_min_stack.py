class MinStack:
    """
    
    beats 40.56%
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        v = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(v)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStackV0(object):
    def __init__(self):
        """
        initialize your data structure here.

        beats 72.87%
        """
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if cur_min is None or x < cur_min:
            cur_min = x
        self.q.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


class MinStack1:
    def __init__(self):
        """
        initialize your data structure here.

        beats 60.25%
        """
        self.data_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        len_data = len(self.data_stack)
        if len_data == 0:
            self.min_stack.append(x)
        else:
            last_min = self.min_stack[-1]
            if x <= last_min:
                self.min_stack.append(x)
        self.data_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.data_stack) > 0 and self.data_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
