class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int

        beats 18.18%
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
