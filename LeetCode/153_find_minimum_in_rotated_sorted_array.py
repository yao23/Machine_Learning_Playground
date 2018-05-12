class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        beats 99.47%
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) / 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]
