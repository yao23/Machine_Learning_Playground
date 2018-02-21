class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        beats 96.67%
        """
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
