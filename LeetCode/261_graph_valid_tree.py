class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        Union-Find
        beats 90.69%
        """
        parent = range(n)

        def find(x):
            return x if parent[x] == x else find(parent[x])

        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y
        return len(edges) == n-1 and all(map(union, edges))

    def validTree1(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        beats 80.86%
        """
        parent = range(n)

        def find(x):
            return x if parent[x] == x else find(parent[x])

        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1

    def validTree2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        DFS
        beats 80.86%
        """
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,

        def visit(v):
            map(visit, neighbors.pop(v, []))

        visit(0)
        return not neighbors

    def validTree3(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        BFS
        beats 99.31%
        """
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        queue = [0]
        for v in queue:
            queue += neighbors.pop(v, [])
        return not neighbors
