import operator


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool

        beats 22.57%
        """
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))

    def isStrobogrammatic1(self, num):
        return all(c + d in '696 00 11 88' for c, d in zip(num, num[::-1]))

    def isStrobogrammatic2(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)))

    def isStrobogrammatic3(self, num):
        return all(map('696 00 11 88'.count, map(operator.add, num, num[::-1])))

    def isStrobogrammatic4(self, num):
        return all(p in '696 00 11 88' for p in map(operator.add, num, num[::-1]))

    def isStrobogrammatic5(self, num):
        return set(map(operator.add, num, num[::-1])) <= set('69 96 00 11 88'.split())

    def isStrobogrammatic6(self, num):
        return set(map(operator.add, num, num[::-1])) <= {'69', '96', '00', '11', '88'}

    def isStrobogrammatic7(self, num):
        return set(map(''.join, zip(num, num[::-1]))) <= {'69', '96', '00', '11', '88'}
