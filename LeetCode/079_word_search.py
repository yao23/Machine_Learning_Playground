class Solution(object):
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        beats 58.20%
        """
        row = len(board)
        col = len(board[0])
        visit = set()

        def dfs(r, c , idx):
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r == row or c == col or (r, c) in visit or board[r][c] != word[idx]:
                return False
            visit.add((r, c))
            res = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1)
            visit.remove((r, c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
    
    def existV0(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        beats 66.79%
        """
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        """
        :param board:
        :param i:
        :param j:
        :param word:
        :return:

        check whether can find word, start at (i,j) position
        """
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit again
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
              or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res
