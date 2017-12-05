class MyQueue(object):
    # beats 10.61%
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.input.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        return self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        if (self.output == []):
            while (self.input != []):
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()