class Node:
    """
    # Definition for a QuadTree node.
    """
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    class Solution:
        def construct(self, grid: List[List[int]]) -> 'Node':
            """
            https://leetcode.com/problems/construct-quad-tree/discuss/274757/Python-Both-Time-and-Space-Beat-100

            :param grid:
            :return:
            """
            def constructTree(grid):
                n = len(grid)

                if n == 1:
                    return Node(grid[0][0], True, None, None, None, None)

                is_leaf = True
                # Check if all elements of the grid are same
                first_value = grid[0][0]
                for l in grid:
                    if l.count(first_value) != n:
                        is_leaf = False
                        break

                if is_leaf:
                    return Node(grid[0][0], True, None, None, None, None)
                else:
                    node = Node('*', False, None, None, None, None)
                    mid = n // 2
                    node.topLeft = constructTree([x[0:mid] for x in grid[0:mid]])
                    node.topRight = constructTree([x[mid:] for x in grid[0:mid]])
                    node.bottomLeft = constructTree([x[0:mid] for x in grid[mid:]])
                    node.bottomRight = constructTree([x[mid:] for x in grid[mid:]])

                    return node

            root = constructTree(grid)

            return root

        def construct2(self, grid):
            """
            https://leetcode.com/problems/construct-quad-tree/discuss/195855/Python-very-simple-recursive-solution-beats-97

            :param grid:
            :return:
            """
            if not grid: return None
            if self.isLeaf(grid):
                return Node(grid[0][0] == 1, True, None, None, None, None)
            n = len(grid)
            mid = n // 2
            return Node('*',
                        False,
                        self.construct([row[:mid] for row in grid[:mid]]),
                        self.construct([row[mid:] for row in grid[:mid]]),
                        self.construct([row[:mid] for row in grid[mid:]]),
                        self.construct([row[mid:] for row in grid[mid:]]))

        def isLeaf(self, grid):
            return all(grid[i][j] == grid[0][0]
                       for i in range(len(grid)) for j in range(len(grid[i])))

        def construct1(self, grid: List[List[int]]) -> 'Node':
            """
            https://leetcode.com/problems/construct-quad-tree/discuss/287123/Python3

            :param grid:
            :return:
            """
            v = [i for j in grid for i in j]
            if set(v) != {0, 1}:
                val = bool(list(set(v))[0])
                is_leaf = True
                top_left = None
                top_right = None
                bottom_left = None
                bottom_right = None
            else:
                val = '*'
                is_leaf = False
                top_left = self.construct([i[:int(len(grid) / 2)] for i in grid[:int(len(grid) / 2)]])
                top_right = self.construct([i[int(len(grid) / 2):] for i in grid[:int(len(grid) / 2)]])
                bottom_left = self.construct([i[:int(len(grid) / 2)] for i in grid[int(len(grid) / 2):]])
                bottom_right = self.construct([i[int(len(grid) / 2):] for i in grid[int(len(grid) / 2):]])
            return Node(val, is_leaf, top_left, top_right, bottom_left, bottom_right)

    def construct0(self, grid: List[List[int]]) -> 'Node':
        """
        my proposed solution

        :param grid:
        :return:
        """
        return self.process(grid, 1)

    def process(self, grid: List[List[int]], node_matrix: List[List[Node]]) -> 'Node':
        n = len(grid)
        if n == 1:
            if len(node_matrix) == 0:  # there is only one element in input grid
                return self.process_node(grid[0][0], True)
            else:  # bottom up to get the root node
                if grid[0][0] == 2:
                    return node_matrix[0][0]
                else:
                    return self.process_node(grid[0][0], True)
        else:
            next_node_matrix = []  # store nodes for next level process
            next_grid = [[]]  # store number in new grid for next level process
            i = 0
            j = 0
            while i < len(grid):
                while j < len(grid[i]):
                    if grid[i[j]] == grid[i[j + 1]] and \
                            grid[i[j + 1]] == grid[i + 1[j]] and \
                            grid[i + 1[j]] == grid[i + 1[j + 1]]:
                        next_grid[i][round(j / 2)] = grid[i[j]]
                        next_node_matrix[i][i] = self.process_node(grid[i[i]], True)
                    else:
                        next_grid[i][round(j / 2)] = 2
                        if node_matrix is not None:
                            node_top_left = node_matrix[i][i]
                            node_top_right = node_matrix[i][i + 1]
                            node_bottom_left = node_matrix[i + 1][i]
                            node_bottom_right = node_matrix[i][i]
                        else:
                            node_top_left = self.process_node(grid[i[j]], True)
                            node_top_right = self.process_node(grid[i[j + 1]], True)
                            node_bottom_left = self.process_node(grid[i + 1[j]], True)
                            node_bottom_right = self.process_node(grid[i + 1[j + 1]], True)
                        next_node_matrix[i][i] = Node('*', False, node_top_left, node_top_right, node_bottom_left,
                                                      node_bottom_right)
                    j += 2

                i += 2

            return self.process(next_grid, next_node_matrix)

    def process_node(self, grid_element: int, is_leaf: bool) -> 'Node':
        val = True if grid_element == 1 else False
        return Node(val, is_leaf, None, None, None, None)
