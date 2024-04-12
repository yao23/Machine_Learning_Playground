class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C++-Java-Python-Ruby

        beats 96.31%
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=ycAq8iqh0TI
        
        beats 14.09%
        """
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

