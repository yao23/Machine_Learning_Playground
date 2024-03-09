class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        DFS
        Runtime:533ms Beats 7.71% of users with Python3
        """
        row = len(grid)
        col = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r,c) in visit:
                return 0
            if r < 0 or c < 0 or r == row or c == col or grid[r][c] == 0:
                return 1
           
            visit.add((r,c))
            res = 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for d in directions:
                dr = r + d[0]
                dc = c + d[1]
                res += dfs(dr, dc)
            return res
               

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r, c)

    def islandPerimeterV0(self, grid: List[List[int]]) -> int:
        """
        BFS
        Runtime:571ms Beats 5.04% of users with Python3
        """
        row = len(grid)
        col = len(grid[0])
        visit = set()
        q = deque()

        res = [0]
        def bfs(r, c):
            q.append((r,c))
            while q:
                size = len(q)
                for i in range(size):
                    r,c = q.popleft()
                    visit.add((r,c))
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for d in directions:
                        dr = r + d[0]
                        dc = c + d[1]
                        if (dr,dc) in visit:
                            continue
                        if dr < 0 or dc < 0 or dr == row or dc == col or grid[dr][dc] == 0:
                            res[0] += 1
                            continue
                        if (dr,dc) not in q:
                            q.append((dr,dc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visit:
                    bfs(r, c)
        return res[0]
