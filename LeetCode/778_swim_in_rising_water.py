class Solution:
    """
    https://www.youtube.com/watch?v=amvrKlMLuGY

    Dijkstra's algorithm

    beats 86.41%
    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]] # height / minTime, r, c
        visit = set((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, (max(t, grid[neiR][neiC]), neiR, neiC)) # max time could be either current max or current value

