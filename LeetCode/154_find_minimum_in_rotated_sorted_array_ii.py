class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        beats 44.10%
        """
        beg = 0
        end = len(nums) - 1
        while beg <= end:
            while beg < end and nums[beg] == nums[beg + 1]:
                beg += 1
            while end > beg and nums[end] == nums[end - 1]:
                end -= 1
            if beg == end:
                return nums[beg]

            mid = (beg + end) / 2
            if nums[mid] > nums[end]:
                beg = mid + 1
            else:
                end = mid

        return nums[beg]
