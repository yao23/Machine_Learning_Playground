class Solution:
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}
        q = deque([(k, 0)])
        dist[k] = 0

        while q:
            node, time = q.popleft()
            if dist[node] < time:
                continue
            for nei, w in adj[node]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    q.append((nei, time + w))

        res = max(dist.values())
        return res if res < float('inf') else -1
