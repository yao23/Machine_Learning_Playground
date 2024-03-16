class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=iJGr1OtmH0c&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=23
        
        Beats 39.88%
        """
        row, col = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            nonlocal res
            if r < 0 or c < 0 or r == row or c == col or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, dfs(r, c))

        return res
