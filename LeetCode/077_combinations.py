from itertools import combinations


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        beats 49.34%
        """
        return list(combinations(range(1, n+1), k))

    def combine1(self, n, k):
        """
        :param n:
        :param k:
        :return:

        Recursive
        """
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n + 1) for pre in self.combine(i - 1, k - 1)]

    def combine2(self, n, k):
        """
        :param n:
        :param k:
        :return:

        Iterative
        """
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        return combs

    def combine3(self, n, k):
        """
        :param n:
        :param k:
        :return:

        Reduce
        """
        return reduce(lambda C, _: [[i] + c for c in C for i in range(1, c[0] if c else n + 1)],
                      range(k), [[]])
