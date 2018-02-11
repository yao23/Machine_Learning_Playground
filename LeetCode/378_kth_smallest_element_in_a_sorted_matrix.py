import bisect
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
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
