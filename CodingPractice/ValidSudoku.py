class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        cell = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]
                if cur == ".":
                    continue
                elif cur in rows[r] or \
                    cur in cols[c] or \
                    cur in cell[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(cur)
                    cols[c].add(cur)
                    cell[(r // 3, c // 3)].add(cur)
                
        return True
