class Solution:
    """
    https://www.youtube.com/watch?v=XQlxCCx2vI4
    
    BFS (faster to find min length)
    
    beats 75.00%
    """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visit = set()
        minHeap = [[0, 0, 0]] # diff, r, c
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue

            visit.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return diff

            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if newR < 0 or newR == rows or newC < 0 or newC == cols or (newR, newC) in visit:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])


