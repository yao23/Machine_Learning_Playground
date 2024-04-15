class Solution:
    """
    https://www.youtube.com/watch?v=cEW05ofxhn0

    beats 79.38%
    """
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list) # adjacency list (k - course, v - prerequisites list
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs] |= dfs(pre) # union hash map
            prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {} # map course -> set indirect prereqs, cache
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
