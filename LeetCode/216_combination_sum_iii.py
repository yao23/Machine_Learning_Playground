from itertools import combinations


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]

        beats 63.91%
        """
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]

    def combinationSum3_1(self, k, n):
        """
        :param k:
        :param n:
        :return:

        Recursive
        """
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in combs(k - 1, n - last, last)]

        return combs(k, n, 10)

    def combinationSum3_2(self, k, n):
        """
        :param k:
        :param n:
        :return:

        Iterative
        """
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]

    def combinationSum3_3(self, k, n):
        """
        :param k:
        :param n:
        :return:

        Reduce
        """
        return [c for c in
                reduce(lambda combs, _: [[first] + comb
                                         for comb in combs
                                         for first in range(1, comb[0] if comb else 10)],
                       range(k), [[]])
                if sum(c) == n]

    def combinationSum3_4(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]

        Backtracking solution
        beats 26.09%
        """

        def dfs(k, target, depth, tmp_res, res):
            len_tmp_res = len(tmp_res)
            if len_tmp_res == k:
                if target == 0:
                    res.append(list(tmp_res))
                else:
                    return
            else:
                for i in range(depth, 10):
                    dfs(k, target - i, i + 1, tmp_res + [i], res)

        res = []
        if n > 0 and k > 0:
            dfs(k, n, 1, [], res)
            return res
        else:
            return res
