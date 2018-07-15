class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Iterative:
        beats 70.72%
        """
        todo, combis = [(n, 2, [])], []
        while todo:
            n, i, combi = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],
                    todo += (n/i, i, combi+[i]),
                i += 1
        return combis

    def getFactors1(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Recursive:
        beats 91.99%
        """

        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n / i],
                    factor(n / i, i, combi + [i], combis)
                i += 1
            return combis

        return factor(n, 2, [], [])
