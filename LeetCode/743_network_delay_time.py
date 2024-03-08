from heapq import *

INF = 1 << 60


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int

        Runtime beats 51.65%
        """
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
    
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int

        beats 77.69%
        """
        delay_list, current_queue = [INF] * (N + 1), [(0, K)]
        delay_list[K] = 0
        neighbor_list = [[] for _ in range(N + 1)]
        for t in times:
            neighbor_list[t[0]] += [(t[2], t[1])]
        while current_queue:
            current_node = heappop(current_queue)[1]
            for neighbor_cost in neighbor_list[current_node]:
                cost = neighbor_cost[0]
                neighbor = neighbor_cost[1]
                neighbor_delay = delay_list[current_node] + cost
                if neighbor_delay < delay_list[neighbor]:
                    delay_list[neighbor] = neighbor_delay
                    heappush(current_queue, (delay_list[neighbor], neighbor))
        return -(INF in delay_list[1:]) or max(delay_list[1:])
