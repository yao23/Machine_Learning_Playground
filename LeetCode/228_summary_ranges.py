class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]

        beats 49.67%
        """
        ranges, r = [], []
        for n in nums:
            if n - 1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

    def summaryRanges1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]

        beats 4.92%
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

    def summaryRanges2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]

        beats 4.92%
        """
        ranges = r = []
        for n in nums:
            if `n - 1` not in r:
                r = []
                ranges += r,
            r[1:] = `n`,
        return map('->'.join, ranges)
