class Solution:
    """
    https://www.youtube.com/watch?v=kPsDTGcrzGM

    Dijkstra's algorithm

    beats 49.43%
    """
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list) # adjacency list with node and success probability
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        maxHeap = [(-1, start_node)] # prob, node (-1 as negative value in maxHeap for Python)
        visit = set()
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            visit.add(node)
            if node == end_node:
                return -prob # maxHeap return negative value
            for nei, neiProb in adj[node]:
                if nei not in visit:
                    heapq.heappush(maxHeap, (prob * neiProb, nei)) # neighbor node with probability
        return 0 # end node not found
