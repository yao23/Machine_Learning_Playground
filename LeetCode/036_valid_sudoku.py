import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        beats 76.16%
        """
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                for i in range(9) for j in range(9)
                for c in [board[i][j]] if c != '.'), [])
        return len(seen) == len(set(seen))

    def isValidSudoku0(self, board):
        return 1 == max(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i / 3, j / 3, c))
        ).values() + [1])

    def isValidSudoku1(self, board):
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))

    def isValidSudoku2(self, board):
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i / 3, j / 3, c)))
