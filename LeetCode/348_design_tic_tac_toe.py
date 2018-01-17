import collections


class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int

        https://leetcode.com/problems/design-tic-tac-toe/discuss/81925/
        beats 50.00%
        """
        self.n = n
        self.rows = [0 for _ in range(n)]
        self.colums = [0 for _ in range(n)]
        self.diag = [0,0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        value = (1.5 - player) * 2
        self.rows[row] += value
        self.colums[col] += value
        if row == col:
            self.diag[0] += value
        if row + col == self.n-1:
            self.diag[1] += value
        if abs(self.rows[row]) == self.n or abs(self.colums[col]) == self.n or abs(self.diag[0]) == self.n or abs(self.diag[1]) == self.n:
            return player
        return 0


class TicTacToe1:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int

        Record the number of moves for each rows, columns, and two diagonals.
        For each move, we -1 for each player 1's move and +1 for player 2's move.
        Then we just need to check whether any of the recorded numbers equal to n or -n.

        https://leetcode.com/problems/design-tic-tac-toe/discuss/81932/
        beats 50.00%
        """
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        offset = player * 2 - 3  # 1 or -1
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0


class TicTacToe2(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int

        https://leetcode.com/problems/design-tic-tac-toe/discuss/81896/
        beats 31.32%
        """
        count = collections.Counter()

        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
