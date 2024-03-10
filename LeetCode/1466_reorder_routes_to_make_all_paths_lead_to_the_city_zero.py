class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=m17yOR5_PpI&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=11
        
        Runtime: 940ms Beats 56.22% of users with Python3
        """
        edges = {(a,b) for (a,b) in connections}
        neighbors = {city:[] for city in range(n)}
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        visit = set()
        changes = 0

        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            for nei in neighbors[city]:
                if nei in visit:
                    continue # do not return here
                
                if (nei,city) not in edges: # road from nei to city
                    changes += 1
                visit.add(nei)
                dfs(nei)
        
        visit.add(0) # process start point 0 first
        dfs(0)
        return changes
