class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
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
                            # print("pos: ", dr, dc)
                            # print("res: ", res[0])
                            continue
                        # print("neighbor: ", dr, dc)
                        if (dr,dc) not in q:
                            q.append((dr,dc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visit:
                    # print("start: ", r, c)
                    # res[0] += 4
                    bfs(r, c)
        return res[0]
