class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        if node v has not been visited, then mark it as 0.
        if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
        if node v has been visited, then mark it as 1.
        If a vertex was marked as 1, then no ring contains v or its successors. (1 in 0 -> 1 <- 3)

        beats 63.48%
        """
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinishV1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        if node v is being visited, return False (a ring found in DFS)
        if neighbor list of node v has been visited (equals empty), then return true.

        Check every course as line 70. (i.e. 1 -> 2,  3 -> 4)

        https://www.youtube.com/watch?v=EgI5nU9etnU&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=2

        beats 65.58%
        """
        map = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            map[crs].append(pre)
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if map[crs] == []:
                return True
            visited.add(crs)
            for pre in map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
