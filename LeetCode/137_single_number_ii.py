class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        @param {integer[]} nums
        @return {integer}
        beats 84.85%
        """
        a = set(nums)
        a = sum(a) * 3 - sum(nums)
        a = a / 2
        return a
