import bisect


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        find smallest two and larger one, then combine them for increasing triplet

        beats 31.52%
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

    def increasingTriplet1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78997/Generalization-in-Python

        bisect_left: insert position for equality

        beats 13.13%
        """
        try:
            inc = [float('inf')] * 2
            for x in nums:
                inc[bisect.bisect_left(inc, x)] = x
            return False
        except:
            return True

    def increasingTriplet2(self, nums):
        """
        :param nums:
        :return:

        beats 21.82%
        """
        inc = [float('inf')] * 2
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= 2:
                return True
            inc[i] = x
        return False

    def increasingSubsequence(self, nums, k):
        """
        :param nums:
        :param k:
        :return:

        for any k >= 0:
        """
        try:
            inc = [float('inf')] * (k - 1)
            for x in nums:
                inc[bisect.bisect_left(inc, x)] = x
            return k == 0
        except:
            return True

    def increasingSubsequence1(self, nums, k):
        inc = [float('inf')] * (k - 1)
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= k - 1:
                return True
            inc[i] = x
        return k == 0
