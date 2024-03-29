import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]

        Recursive
        beats 87.08%
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

    def findItinerary1(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]

        Iterative
        beats 72.35%
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]
