class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        beats 19.14%
        """
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i % 2)
