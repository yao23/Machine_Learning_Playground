class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        @param a list of integers
        @return an integer
        beats 89.72%
        """
        if not nums:
            return 0

        new_tail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]

        return new_tail + 1
