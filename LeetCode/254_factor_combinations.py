class Solution(object):
    # Iterative:
    # beats 70.72%
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
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

    # Recursive:
    # beats 91.99%
    def getFactors1(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n / i],
                    factor(n / i, i, combi + [i], combis)
                i += 1
            return combis

        return factor(n, 2, [], [])