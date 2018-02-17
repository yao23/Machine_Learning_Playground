class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Build it inside-out
        Start with the empty matrix, add the numbers in reverse order until we added the number 1.
        Always rotate the matrix clockwise and add a top row:

        beats 40.09%
        """
        res, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(res), lo
            res = [range(lo, hi)] + zip(*res[::-1])
        return res

    def generateMatrix1(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Walk the spiral
        Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n.
        Make a right turn when the cell ahead is already non-zero.

        beats 76.91%
        """
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n * n):
            res[i][j] = k + 1
            if res[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return res

    def generateMatrix2(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        Ugly inside-out
        Same as solution 0, but without helper variables.Saves a line, but makes it ugly.Also, because
        I access A[0][0], I had to handle the n = 0 case differently.

        beats 91.72%
        """
        res = [[n * n]]
        while res[0][0] > 1:
            res = [range(res[0][0] - len(res), res[0][0])] + zip(*res[::-1])
        return res * (n > 0)
