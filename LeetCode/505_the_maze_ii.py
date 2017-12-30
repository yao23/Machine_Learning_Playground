import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        https://leetcode.com/articles/the-maze-ii/
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

        https://leetcode.com/problems/the-maze-ii/discuss/98409/
        This is a typical problem where we can use uniform-cost search algorithm(Dijkstra's algorithm).
        We should note that whenever we update the distance of a node that is already in the max-heap,
        we need to re-heapify the max-heap to retain the heap invariance.

        beats 100.00%
        """
        root = [0, tuple(start)]
        queue = [root]
        # save the reference of the corresponding node of a state, for fast look-up
        node_ref = {tuple(start): root}
        # save the shortest distance from start to every other state, you can also regard it as a visited set
        min_dist = {tuple(start): 0}
        while len(queue):
            # when a node is popped out, the shortest distance from start to this node is found
            cur_dist, state = heapq.heappop(queue)
            # add it to min_dist
            min_dist[state] = cur_dist
            x, y = state
            # remove it from node_ref
            node_ref.pop(state)
            if list(state) == destination:
                return cur_dist
            modified = False
            tmp_y = y
            dist = 0
            while tmp_y > 0 and maze[x][tmp_y - 1] != 1:  # roll left
                dist += 1
                tmp_y -= 1
            # if shortest distance to (i, tmp_y) is not found((i, tmp_y) is not visited), update the distance
            if (x, tmp_y) not in min_dist:
                # if state is not in max-heap, then create a node to represent it and push it into max-heap,
                # and save the node's reference in node_ref
                if (x, tmp_y) not in node_ref:
                    node = [cur_dist + dist, (x, tmp_y)]
                    node_ref[(x, tmp_y)] = node
                    heapq.heappush(queue, node)
                # if state is in max-heap, update it distance
                else:
                    # we modify the corresponding node in the max-heap
                    modified = True
                    node = node_ref[(x, tmp_y)]
                    node[0] = min(node[0], cur_dist + dist)
            tmp_x = x
            dist = 0
            while tmp_x > 0 and maze[tmp_x - 1][y] != 1:  # roll up
                dist += 1
                tmp_x -= 1
            if (tmp_x, y) not in min_dist:
                if (tmp_x, y) not in node_ref:
                    node = [cur_dist + dist, (tmp_x, y)]
                    node_ref[(tmp_x, y)] = node
                    heapq.heappush(queue, node)
                else:
                    modified = True
                    node = node_ref[(tmp_x, y)]
                    node[0] = min(node[0], cur_dist + dist)
            tmp_y = y
            dist = 0
            while tmp_y < len(maze[0]) - 1 and maze[x][tmp_y + 1] != 1:  # roll right
                dist += 1
                tmp_y += 1
            if (x, tmp_y) not in min_dist:
                if (x, tmp_y) not in node_ref:
                    node = [cur_dist + dist, (x, tmp_y)]
                    node_ref[(x, tmp_y)] = node
                    heapq.heappush(queue, node)
                else:
                    modified = True
                    node = node_ref[(x, tmp_y)]
                    node[0] = min(node[0], cur_dist + dist)
            tmp_x = x
            dist = 0
            while tmp_x < len(maze) - 1 and maze[tmp_x + 1][y] != 1:  # roll down
                dist += 1
                tmp_x += 1
            if (tmp_x, y) not in min_dist:
                if (tmp_x, y) not in node_ref:
                    node = [cur_dist + dist, (tmp_x, y)]
                    node_ref[(tmp_x, y)] = node
                    heapq.heappush(queue, node)
                else:
                    modified = True
                    node = node_ref[(tmp_x, y)]
                    node[0] = min(node[0], cur_dist + dist)
            # if some nodes in the max-heap are modified, then heapify the max-heap to retain the heap invariance
            if modified:
                heapq.heapify(queue)
        return -1
