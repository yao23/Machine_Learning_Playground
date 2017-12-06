from itertools import combinations

class Solution(object):
    # beats 63.91%
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]

    # Recursive
    def combinationSum3_1(self, k, n):
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in combs(k - 1, n - last, last)]

        return combs(k, n, 10)

    # Iterative
    def combinationSum3_2(self, k, n):
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]

    # Reduce
    def combinationSum3_3(self, k, n):
        return [c for c in
                reduce(lambda combs, _: [[first] + comb
                                         for comb in combs
                                         for first in range(1, comb[0] if comb else 10)],
                       range(k), [[]])
                if sum(c) == n]