import heapq
from heapq import heappop, heappush, heapify

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

    def shortestDistance1(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        beats 100.00%
        """
        root = [0, tuple(start)]
        queue = [root]
        # save the reference of the corresponding node of a state, for fast look-up
        node_ref = {tuple(start): root}
        # save the shortest distance from start to every other state, you can also regard it as a visited set
        min_dist = {tuple(start):0}
        while len(queue):
            # when a node is popped out, the shortest distance from start to this node is found
            d, state = heappop(queue)
            # add it to min_dist
            min_dist[state] = d
            i, j = state
            # remove it from node_ref
            node_ref.pop(state)
            if list(state) == destination:
                return d
            modified = False
            t_j = j
            dist = 0
            while t_j > 0 and maze[i][t_j - 1] != 1:  # roll left
                dist += 1
                t_j -= 1
            # if shortest distance to (i, t_j) is not found((i, t_j) is not visited), update the distance
            if (i, t_j) not in min_dist:
                # if state is not in max-heap, then create a node to represent it and push it into max-heap,
                # and save the node's reference in node_ref
                if (i, t_j) not in node_ref:
                    node = [d + dist, (i, t_j)]
                    node_ref[(i, t_j)] = node
                    heappush(queue, node)
                # if state is in max-heap, update it distance
                else:
                    # we modify the corresponding node in the max-heap
                    modified = True
                    node = node_ref[(i, t_j)]
                    node[0] = min(node[0], d + dist)
            t_i = i
            dist = 0
            while t_i > 0 and maze[t_i - 1][j] != 1:  # roll up
                dist += 1
                t_i -= 1
            if (t_i, j) not in min_dist:
                if (t_i, j) not in node_ref:
                    node = [d + dist, (t_i, j)]
                    node_ref[(t_i, j)] = node
                    heappush(queue, node)
                else:
                    modified = True
                    node = node_ref[(t_i, j)]
                    node[0] = min(node[0], d + dist)
            t_j = j
            dist = 0
            while t_j < len(maze[0]) - 1 and maze[i][t_j + 1] != 1:  # roll right
                dist += 1
                t_j += 1
            if (i, t_j) not in min_dist:
                if (i, t_j) not in node_ref:
                    node = [d + dist, (i, t_j)]
                    node_ref[(i, t_j)] = node
                    heappush(queue, node)
                else:
                    modified = True
                    node = node_ref[(i, t_j)]
                    node[0] = min(node[0], d + dist)
            t_i = i
            dist = 0
            while t_i < len(maze) - 1 and maze[t_i + 1][j] != 1:  # roll down
                dist += 1
                t_i += 1
            if (t_i, j) not in min_dist:
                if (t_i, j) not in node_ref:
                    node = [d + dist, (t_i, j)]
                    node_ref[(t_i, j)] = node
                    heappush(queue, node)
                else:
                    modified = True
                    node = node_ref[(t_i, j)]
                    node[0] = min(node[0], d + dist)
            # if some nodes in the max-heap are modified, then heapify the max-heap to retain the heap invariance
            if modified:
                heapify(queue)
        return -1
