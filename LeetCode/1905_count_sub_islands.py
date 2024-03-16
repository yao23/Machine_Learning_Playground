class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=mLpW3qfbNJ8&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=18
        
        Beats 47.76%
        """
        row, col = len(grid1), len(grid1[0])
        visit = set()
        cnt = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == col or grid2[r][c] == 0 or (r, c) in visit:
                return True
            res = True
            if grid1[r][c] == 0: # not sub-island in grid1
                res = False
            visit.add((r, c))
            res = dfs(r + 1,c) and res
            res = dfs(r - 1,c) and res
            res = dfs(r,c + 1) and res
            res = dfs(r,c - 1) and res
            return res

        for r in range(row):
            for c in range(col):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    cnt += 1
        return cnt
