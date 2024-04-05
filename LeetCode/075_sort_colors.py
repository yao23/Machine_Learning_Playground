class Solution(object):
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        https://www.youtube.com/watch?v=4xbWSRZHqac

        bucket sort

        beats 46.30%
        """
        # Assuming arr only contains 0, 1 or 2
        counts = [0, 0, 0]

        # Count the quantity of each val in arr
        for n in nums:
            counts[n] += 1
        
        # Fill each bucket in the original array
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return nums
        
    def sortColorsV0(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        beats 96.67%
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1

    def sortColorsV1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        quick select / sort

        https://www.youtube.com/watch?v=4xbWSRZHqac

        beats 18.71%
        """
        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
