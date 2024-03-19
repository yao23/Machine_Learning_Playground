class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=nIVW4P8b1VA&list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&index=8
        
        beats 95.66%
        """
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]: # left is sorted, right is unsorted
                l = m + 1
            else: # left is unsorted, right is sorted
                r = m - 1
        return res
        
    def findMin0(self, nums):
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
