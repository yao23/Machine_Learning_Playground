# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    """
    In my opinion an iterator shouldn't copy the entire data (which some solutions have done) but just iterate over
    the original data structure.

    I keep the current progress in a stack. My hasNext tries to find an integer. My next returns it and moves on.
    I call hasNext in next because hasNext is optional. Some user of the iterator might call only next and
    never hasNext, e.g., if they know how many integers are in the structure or if they want to handle the ending with
    exception handling.

    https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80146/Real-iterator-in-Python-Java-C++
    """
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        beats 29.12%
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        nested_list, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nested_list[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            nested_list, i = s[-1]
            if i == len(nested_list):
                s.pop()
            else:
                x = nested_list[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


class NestedIterator1(object):
    """
    Generator

    https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80247/Python-Generators-solution

    beats 83.76%
    """
    def __init__(self, nestedList):
        self.peek = None

        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y

        self.gen = gen(nestedList)

    def next(self):
        if self.peek is None:
            return next(self.gen)
        else:
            tmp = self.peek
            self.peek = None
            return tmp

    def hasNext(self):
        if self.peek is None:
            try:
                self.peek = next(self.gen)
                return True
            except StopIteration:
                return False
        else:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
