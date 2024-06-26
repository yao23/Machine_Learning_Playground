class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int

        beats 17.02%
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
