class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=YnxUdAO7TAo

        beats 72.66%
        """
        if grid[0][0] == 1:
            return -1
        row, col = len(grid), len(grid[0])
        length = 1
        q = deque()
        q.append((0, 0))
        visit = set()
        directions = [[1,1],[1,0],[0,1],[-1,1],[1,-1],[-1,0],[0,-1],[-1,-1]]

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if x == row - 1 and y == col - 1:
                    return length

                for dx,dy in directions:
                    x1, y1 = x + dx, y + dy
                    if x1 < 0 or y1 < 0 or x1 == row or y1 == col or (x1, y1) in visit or grid[x1][y1] == 1:
                        continue
                    else:
                        visit.add((x1,y1))
                        q.append((x1,y1))
            length += 1

        return -1
