class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        in-place
        beats 90.50%
        """
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    """
    beats 57.93%
    """
    def moveZeroesV1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if not nums or length == 0:
            return nums

        l = 0
        for r in range(length):
            if nums[r] != 0: # find non-zero
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return nums
        
    """
    beats 26.72%
    """
    def moveZeroesV0(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if not nums or length == 0:
            return nums

        l, r = 0, 0
        while l < length and r < length:
            while l < length and nums[l] != 0: # find zero
                l += 1

            while r < length and nums[r] == 0: # find non-one
                r += 1

            if l < length and r < length and l < r: # switch if zero element in left and non-zero right
                nums[l], nums[r] = nums[r], nums[l]
            elif r <= l: # moveing right if non-zero element in left and zero right
                r += 1
                while r < length and nums[r] == 0: # find non-one
                    r += 1

        return nums
