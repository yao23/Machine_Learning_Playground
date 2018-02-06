class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        beats 60.70%
        """
        return len([x for x in nums if x < target])
