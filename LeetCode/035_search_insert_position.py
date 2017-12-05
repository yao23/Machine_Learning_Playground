class Solution(object):
    # beats 60.70%
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([x for x in nums if x<target])