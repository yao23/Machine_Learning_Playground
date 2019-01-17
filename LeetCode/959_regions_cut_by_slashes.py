class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int

        beats 18.18%

        Split a cell in to 4 parts like this.
        We give it a number top is 1, right is 2, bottom is 3 left is 4.
        ---------
        |\     /|
        | \   / |
        |  \ /  |
        |   /\  |
        |  /  \ |
        | /    \|
        ---------

        Two adjacent parts in different cells are contiguous regions.
        In case '/', top and left are contiguous, bottom and right are contiguous.
        In case '\\', top and right are contiguous, bottom and left are contiguous.
        In case ' ', all 4 parts are contiguous.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))

    def regionsBySlashes1(self, grid):
        """
        :type grid: List[str]
        :rtype: int

        beats 68.18%
        """
        def dfs(i, j, k):
            if 0 <= i < n > j >= 0 and not matrix[i][j][k]:
                if grid[i][j] == "*":
                    if k <= 1:
                        matrix[i][j][0] = matrix[i][j][1] = cnt
                        dfs(i - 1, j, 2)
                        dfs(i, j + 1, 3)
                    else:
                        matrix[i][j][2] = matrix[i][j][3] = cnt
                        dfs(i + 1, j, 0)
                        dfs(i, j - 1, 1)
                elif grid[i][j] == "/":
                    if 1 <= k <= 2:
                        matrix[i][j][1] = matrix[i][j][2] = cnt
                        dfs(i, j + 1, 3)
                        dfs(i + 1, j, 0)
                    else:
                        matrix[i][j][0] = matrix[i][j][3] = cnt
                        dfs(i - 1, j, 2)
                        dfs(i, j - 1, 1)
                else:
                    matrix[i][j][0] = matrix[i][j][1] = matrix[i][j][2] = matrix[i][j][3] = cnt
                    dfs(i - 1, j, 2)
                    dfs(i, j + 1, 3)
                    dfs(i + 1, j, 0)
                    dfs(i, j - 1, 1)

        grid, n = [row.replace("\\", "*") for row in grid], len(grid)
        matrix, cnt = [[[0, 0, 0, 0] for j in range(n)] for i in range(n)], 0
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not matrix[i][j][k]:
                        cnt += 1
                        dfs(i, j, k)
        return cnt

    def regionsBySlashes2(self, grid):
        """
        :type grid: List[str]
        :rtype: int

        beats 31.82%
        """
        grid_len = len(grid)
        g = [[0] * grid_len * 3 for _ in range(grid_len * 3)]
        # draw lines as squares on 2x2 grid. These will be walls for the flood fill
        for i in range(grid_len):
            for j in range(grid_len):
                if grid[i][j] == '/':
                    g[3 * i + 2][3 * j] = 1
                    g[3 * i + 1][3 * j + 1] = 1
                    g[3 * i][3 * j + 2] = 1
                elif grid[i][j] == '\\':
                    g[3 * i][3 * j] = 1
                    g[3 * i + 1][3 * j + 1] = 1
                    g[3 * i + 2][3 * j + 2] = 1
        # check it out
        """for i in range(l*3):
            print g[i]"""

        # Flood Fill grid, count new regions
        visited = set()
        to_check = []
        regions = 0
        # Indexing is not straight forward;
        # you could check every 0 on the 3*l x 3*l grid, but that will take a constant factor longer.
        # Only need to check directly left and right of middle, to find every possible region and also guarantees
        # that the starting point is not a wall.
        for i in range(grid_len):
            for j in range(grid_len):
                for k in range(2):
                    if (3 * i + 1, 3 * j + 2 * k) not in visited:
                        # print i, j
                        to_check.append((i * 3 + 1, j * 3 + 2 * k))
                        while to_check:
                            temp = to_check.pop()
                            if temp in visited:
                                continue
                            x = temp[0]
                            y = temp[1]
                            # check down, up, left, right
                            if x > 0 and g[x - 1][y] != 1:
                                to_check.append((x - 1, y))
                            if x < grid_len * 3 - 1 and g[x + 1][y] != 1:
                                to_check.append((x + 1, y))
                            if y > 0 and g[x][y - 1] != 1:
                                to_check.append((x, y - 1))
                            if y < grid_len * 3 - 1 and g[x][y + 1] != 1:
                                to_check.append((x, y + 1))
                            visited.add(temp)
                        regions += 1
        return regions
