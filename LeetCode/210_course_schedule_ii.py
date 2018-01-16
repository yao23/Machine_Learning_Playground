import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        DFS
        beats 79.58%
        """
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in xrange(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:  # no more prerequisite
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []

    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        dic: prerequisites hash map whose value is set

        BFS
        beats 48.77%
        """
        dic = {i: set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:  # no more prerequisite
                    queue.append(i)
        return res if count == numCourses else []
