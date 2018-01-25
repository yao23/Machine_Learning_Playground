class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        beats 75.55%
        """
        return len(nums) != len(set(nums))
