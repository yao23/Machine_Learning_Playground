import bisect
import heapq


class Solution(object):
    """
    TikTok
    
    https://www.youtube.com/watch?v=0d6WF79hQME
    
    beats 80.04%
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def lessK(m):
            cnt = 0
            for i in range(N):
                x = bisect_right(matrix[i], m) # insert m into current row matrix[i] and keep sorted after insertion, return right-most index to insert m
                cnt += x
            return cnt # how many elements smaller than m

        while l < r:
            mid = (l + r) // 2
            if lessK(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l
        
    def kthSmallestV4(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        https://discuss.leetcode.com/topic/52912/binary-search-heap-and-sorting-comparison-with-concise-code-and-1-liners-python-72-ms

        binary search

        time: O(n * log(n) * log(N)), where N is the search space that ranges from the smallest element to the biggest
        one. You can argue that int implies N = 2^32, log(N) is constant. In a way, this is an O(n * log(n)) solution.

        space: O(1)

        beats 82.46%
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        heap

        time: O(k * log n), so the worst-case and average-case time complexity is O(n^2 * log n)
        space: O(n)

        beats 31.97%
        """
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return ret

    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        sorting

        beats 59.18%
        """
        res_list = []
        for row in matrix:
            res_list += row
        return sorted(res_list)[k - 1]

    """
    https://www.youtube.com/watch?v=0d6WF79hQME
    
    beats 62.03%
    """
    def kthSmallestV3(self, matrix: List[List[int]], k: int) -> int:
        flatList = [] # flat 2D matrix to 1D list
        for row in matrix:
            flatList.extend(row)
        flatList.sort()
        return flatList[k - 1]
