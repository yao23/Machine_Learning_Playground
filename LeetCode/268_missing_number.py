class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        beats 99.07%
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)
