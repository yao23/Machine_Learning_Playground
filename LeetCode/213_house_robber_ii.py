class Solution(object):
    # beats 89.67%
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))