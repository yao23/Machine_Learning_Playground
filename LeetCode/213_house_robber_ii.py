class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://leetcode.com/problems/house-robber-ii/discuss/59934/
        the idea is similar like House Robber (LC 198)
        the tricky part is pick first one or not will influence last one
        so it will get max from with first one (rob(nums[:-1])) or without first one (rob(nums[len(nums) != 1:]))

        beats 89.67%
        """
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))  # False equals 0 and True equals 1
