class Solution(object):
    # beats 65.04%
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

    # beats 49.12%
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return reduce(lambda m, (i, n): max(m, i + n) * (i <= m), enumerate(nums, 1), 1) > 0

    # beats 98.78%
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal