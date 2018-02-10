class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        nums: [1, 5, 1, 1, 6, 4]
        sort: [1, 1, 1, 4, 5, 6]
        nums[half::-1] => [1, 1, 1]
        nums[:half:-1] => [6, 5, 4]

        beats 96.09%
        """
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

    def wiggleSort1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        nums: [1, 5, 1, 1, 6, 4]
        sort: [1, 1, 1, 4, 5, 6]
        nums[:half][::-1] => [1, 1, 1]
        nums[half:][::-1] => [6, 5, 4]

        beats 48.53%
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
