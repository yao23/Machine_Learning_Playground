class Solution(object):
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        https://www.youtube.com/watch?v=9z2BunfoZ5Y&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=21

        Beats 94.62%
        """
        row, col = len(board), len(board[0])

        # 1. (DFS) capture unsurrounded
        def dfs(r, c):
            if r < 0 or c < 0 or r == row or c == col or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 2. capture surrounded regions (O => X)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and r in [0, row -1 ] or c in [0, col - 1]:
                    dfs(r, c)

        # 3. capture unsurrounded regions (T => O)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
    def solve0(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.

        Phase 1: "Save" every O-region touching the border, changing its cells to 'S'.
        Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.
        beats 97.42%
        """
        if not any(board):
            return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
