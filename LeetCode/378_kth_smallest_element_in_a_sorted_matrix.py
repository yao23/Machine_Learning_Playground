# https://discuss.leetcode.com/topic/52912/binary-search-heap-and-sorting-comparison-with-concise-code-and-1-liners-python-72-ms
class Solution(object):
    # beats 82.46%
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo