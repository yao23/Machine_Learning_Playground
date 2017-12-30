import heapq


class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        beats 66.67%
        """
        dest = tuple(destination)
        m = len(maze)
        n = len(maze[0])

        def go(start_point, direction_xy):
            # return the stop position and length
            start_x, start_y = start_point
            delta_x, delta_y = direction_xy
            len_res = 0
            while 0 <= start_x + delta_x < m and 0 <= start_y + delta_y < n \
                    and maze[start_x + delta_x][start_y + delta_y] != 1:
                start_x += delta_x
                start_y += delta_y
                len_res += 1
            return len_res, (start_x, start_y)
        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited = {}
        q = []
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            if cur in visited and visited[cur] <= length:
                continue  # if cur is visited and with a shorter length, skip it.
            visited[cur] = length
            if cur == dest:
                return length
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
                cur_len, np = go(cur, direction)
                heapq.heappush(q, (length + cur_len, np))
        return -1
