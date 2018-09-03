class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.

        BFS (start from gate who is r in the code and represented as 0)

        beats 78.90%
        """
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        for i, j in q:
            for row_index, col_index in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):  # top/bottom/left/right node
                if 0 <= row_index < len(rooms) and 0 <= col_index < len(rooms[0]) \
                        and rooms[row_index][col_index] > 2 ** 30:
                    rooms[row_index][col_index] = rooms[i][j] + 1
                    q += (row_index, col_index),

    def wallsAndGates1(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.

        DFS (start from gate who is r in the code and represented as 0)

        beats 31.25%
        """
        s = [(i, j, 0) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        while s:
            i, j, step = s.pop()
            rooms[i][j] = step if rooms[i][j] > step else rooms[i][j]
            for row_index, col_index in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= row_index < len(rooms) and 0 <= col_index < len(rooms[0]) \
                        and rooms[row_index][col_index] > step:
                    s += (row_index, col_index, step + 1),
