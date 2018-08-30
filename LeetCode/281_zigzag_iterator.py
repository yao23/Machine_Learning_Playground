import itertools


class ZigzagIterator(object):
    """
    With a list of remaining downcounter + iterator pairs:
    beats 87.23%
    """
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        """
        :rtype: int
        """
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)


class ZigzagIterator1(object):
    # With a generator expression and a down counter:
    def __init__(self, v1, v2):
        self.vals = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0


class ZigzagIterator2(object):
    # With a generator function and a down counter:
    def __init__(self, v1, v2):
        def vals():
            for i in itertools.count():
                for v in v1, v2:
                    if i < len(v):
                        yield v[i]
        self.vals = vals()
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
