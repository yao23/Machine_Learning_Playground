class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=f7JOBJIC-NA&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=17

        Minimum Spanning Tree (MST) - Prim's Algorithm 
        Beats 32.02%
        """
        N = len(points)
        adj = {i:[] for i in range(N)} # i: [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dis = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])

        # Prim's 
        res = 0
        visit = set()
        minHeap = [[0, 0]] # [cost, node]
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res
