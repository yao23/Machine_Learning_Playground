class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        find longest non-increasing suffix

        beats 56.45%
        """

        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)
        # find pivot
        pivot = right - 1
        successor = 0
        # find rightmost successor
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        # reverse suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
