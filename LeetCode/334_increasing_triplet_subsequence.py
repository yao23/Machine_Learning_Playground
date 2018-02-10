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

        beats 13.13%
        """
        try:
            inc = [float('inf')] * 2
            for x in nums:
                inc[bisect.bisect_left(inc, x)] = x
            return False
        except:
            return True
