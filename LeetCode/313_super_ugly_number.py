import heapq
import itertools


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int

        beats 84.85%
        """
        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        map(uglies.append, itertools.islice(uniqed, n-1))
        return uglies[-1]

    def nthSuperUglyNumber1(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int

        beats 85.23%
        """
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime

        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]
