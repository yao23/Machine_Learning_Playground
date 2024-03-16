class Solution(object):
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not edges:
            return False
        adj = {i:[] for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        visit = set()

        def dfs(cur, pre):
            if cur in visit:
                return False

            visit.add(cur)
            for nei in adj[cur]:
                if nei == pre:
                    continue
                if not dfs(nei, cur):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)

    
    def validTree0(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        if there is loop, num_edges > num_vertex - 1
        if there is island, num_edges < num_vertex - 1

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

        if there is no loop, num_edges = num_vertex - 1
        if there is no island vertex left after traversal, it's a valid tree

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
