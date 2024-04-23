class Solution(object):
    """
    https://www.youtube.com/watch?v=pV2kpPD66nE
    
    DFS

    beats 5.18%
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        numIslands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    numIslands += 1
                    dfs(r, c)
        return numIslands
        
    def numIslandsV2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Graph traversal (DFS, BFS) and update visited node

        beats 20.33%
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

    def numIslandsV1(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int

        Graph traversal (DFS) and update visited node

        beats 67.93%
        """
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(x, y):
            if grid[x][y] == "0" or (x * col + y) in visited:
                return
            
            visited.add(x * col + y)
            if x + 1 < row:
                dfs(x + 1, y)
            if y + 1 < col:
                dfs(x, y + 1)
            if x - 1 >= 0:
                dfs(x - 1, y)
            if y - 1 >= 0:
                dfs(x, y - 1)

        cnt = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1" and (x * col + y) not in visited:
                    cnt += 1
                    dfs(x, y)
        return cnt

    """
    BFS 

    beats 6.31%
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        row = len(grid)
        col = len(grid[0])
        visited = set()
        q = collections.deque()

        def bfs(x, y):
            if grid[x][y] == "0" or (x, y) in visited:
                return
            
            visited.add((x, y))
            q.append((x, y))
            while q:
                x, y = q.popleft() # dfs if change to q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for d in directions:
                    dx = x + d[0]
                    dy = y + d[1]
                    if dx in range(row) and dy in range(col):
                        if (dx, dy) not in visited and grid[dx][dy] == "1":
                            visited.add((dx, dy))
                            q.append((dx, dy))

        cnt = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1" and (x, y) not in visited:
                    cnt += 1
                    bfs(x, y)
        return cnt
